import uvicorn

import config

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host=config.API_HOST,
        port=int(config.API_PORT),
        log_level='info',
        reload=True,
    )
