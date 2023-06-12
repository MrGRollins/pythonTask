import uvicorn
from fastapi import FastAPI
import asyncio
import sys
from elastic_search.api import shop_api, admin_api

app = FastAPI(
    docs_url='/api/docs'
)
admin_app = FastAPI(
    docs_url='/api/docs/admin'
)

app.include_router(shop_api.router, prefix="/api/shop_api")
admin_app.include_router(admin_api.router, prefix="/api/admin_api")


async def create_webserver(port):
    server_config = uvicorn.Config("main:app", port=port, log_level="info")
    server = uvicorn.Server(server_config)
    await server.serve()

async def create_webserver1(port):
    server_config = uvicorn.Config("main:admin_app", port=port, log_level="info")
    server = uvicorn.Server(server_config)
    await server.serve()


async def main():
    done, pending = await asyncio.wait(
        [
            create_webserver(8002),
            create_webserver1(8003),
        ],
        return_when=asyncio.FIRST_COMPLETED,
    )

    print("done")
    print(done)
    print("pending")
    print(pending)
    for pending_task in pending:
        pending_task.cancel("Another service died, server is shutting down")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
        sys.exit(0)