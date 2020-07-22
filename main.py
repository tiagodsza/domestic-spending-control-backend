import uvicorn

from app.core.database import engine, DeclarativeBase

if __name__=='__main__':
    DeclarativeBase.metadata.create_all(bind=engine)
    uvicorn.run(
        'app:app',
        host='localhost',
        log_level='info',
        reload=True,
    )