from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from ..schemas.gesture import GestureEvent, GestureRecognition

router = APIRouter(tags=["gestures"])


class GestureConnectionManager:
    def __init__(self) -> None:
        self.active: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket) -> str:
        await websocket.accept()
        session_id = str(uuid4())
        self.active[session_id] = websocket
        return session_id

    def disconnect(self, session_id: str) -> None:
        self.active.pop(session_id, None)


manager = GestureConnectionManager()


@router.websocket("/ws/gestures")
async def gesture_stream(websocket: WebSocket) -> None:
    session_id = await manager.connect(websocket)
    await websocket.send_json({"type": "connected", "session_id": session_id})
    try:
        while True:
            payload = await websocket.receive_json()
            try:
                event = GestureEvent.model_validate(payload)
                recognition = GestureRecognition(
                    gesture=event.gesture,
                    confidence=event.confidence,
                    accepted=event.confidence >= 0.7,
                    received_at=datetime.now(timezone.utc),
                )
                await websocket.send_json({"type": "gesture", "data": recognition.model_dump(mode="json")})
            except ValueError as error:
                await websocket.send_json({"type": "error", "detail": str(error)})
    except WebSocketDisconnect:
        manager.disconnect(session_id)
