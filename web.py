
import asyncio
import websockets
import datetime

async def handler(websocket, path):
    try:
        last_time_sent = datetime.datetime.now()  # 前回メッセージを送信した時刻を記録
        while True:
            # 現在の時刻を取得
            current_time = datetime.datetime.now()
            time_str = current_time.strftime("%H:%M:%S")
            
            # 10分ごとに「10分経過」というメッセージを送信
            if current_time - last_time_sent >= datetime.timedelta(minutes=10):
                await websocket.send("10分経過")
                last_time_sent = current_time
            
            # 現在の時刻を送信
            await websocket.send(time_str)
            
            # クライアントからのメッセージを受信
            try:
                message = await asyncio.wait_for(websocket.recv(), timeout=1)
                print(f"Received message: {message}")
                
                # 受信したメッセージを返信
                await websocket.send(f"Received message: {message}")
            except asyncio.TimeoutError:
                pass
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected")  # クライアントが切断されたことを表示

async def main():
    async with websockets.serve(handler, "localhost", 8001):
        # サーバーが起動したことを表示
        print("WebSocket server started...")
        # イベントループを永久に実行
        await asyncio.Future()  # これによりイベントループが永遠に実行されます

asyncio.get_event_loop().run_until_complete(main())