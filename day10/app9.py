import asyncio
import edge_tts

TEXT = "Vanakkam, Gundama. naan than soso.. Saapadu Sapidalama?"

# TEXT = "vanakkam, Hello, welcome to Learn Less Daily."

async def main():
    communicate = edge_tts.Communicate(
        TEXT,
        voice="ta-IN-PallaviNeural"
    )
    await communicate.save("output.mp3")

asyncio.run(main())