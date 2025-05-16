from app.core.settings import get_settings
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.ext.asyncio.session import async_sessionmaker
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

SETTINGS = get_settings()
#
engine = AsyncEngine(
    create_engine(
        SETTINGS.DB_URL,
        echo=SETTINGS.LOG_LEVEL == "DEBUG",
        future=True,
    )
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
