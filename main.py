import uvicorn

from app.database import engine, DeclarativeBase
import config

if __name__=='__main__':
    DeclarativeBase.metadata.create_all(bind=engine)
    uvicorn.run(
        'app:app',
        host= config.HOST,
        port=int(config.PORT),
        log_level='info',
        reload=True,
    )