import os
import glob
import asyncio
from typing import List
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module='torch')


# Function to chunk text into smaller pieces
def chunk_text(text: str, size: int, overlap: int) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(len(text), start+size)
        chunks.append(text[start:end])
        start += size  - overlap
    return chunks

# Asynchronous file reading functions
async def read_file(path: str) -> str:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor (none, lambda: open(path, "r", encoding="utf-8").read())

# Asynchronous processing of files
async def process_file(path: str) -> List[str]:
    text = await read_file(path)
    return chunk_text(text, 500, 50)

# Main Function to gather all files and process them asynchronously
async def main():
    files = glob.glob(os.path.join('folder',".txt"))
    if not files:
        print('No Supported files found')
        return 

    # Print the number of files found and start processing them
    print(f"Found {len(files)} files.")
    results = await asuncio.gather(*(process_file(f) for f in files))
    
    # Flatten the list
    all_chunks = [chunk for chunks in results for chunk in chunks]
    
    print(f"Total Chunks: {len(all_chunks)}")



if __name__ == "__main__":
    asyncio.run(main())