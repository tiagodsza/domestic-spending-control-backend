import uvicorn

from app.database import engine, DeclarativeBase
import config

if __name__=='__main__':
    DeclarativeBase.metadata.create_all(bind=engine)
    uvicorn.run(
        'app:app',
        host= config.API_HOST,
        port=int(config.API_PORT),
        log_level='info',
        reload=True,
    )