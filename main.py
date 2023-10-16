from enum import IntEnum

from fastapi import FastAPI, Depends
from pydantic import BaseModel
import typing as t

from sqlalchemy.orm import Session

import models, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Switching Service",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class SourceTypeEnum(IntEnum):
    # data
    unknown = 0
    video = 1
    audio = 2
    data = 3


class SourceObject(BaseModel):
    display_name: str
    source_type: SourceTypeEnum = SourceTypeEnum.unknown
    address: str


class DestinationObject(BaseModel):
    display_name: str
    address: str


class DestinationCreateRequest(DestinationObject):
    pass


class Destination(DestinationObject):
    uid: str


class SourceCreateRequest(SourceObject):
    pass


class Source(SourceObject):
    uid: str


class SourceGroupObject(BaseModel):
    display_name: str = ""
    video_uid: str
    audio_uid: str
    data_uid: str


class SourceGroupCreateRequest(SourceGroupObject):
    pass


class SourceGroup(SourceGroupObject):
    uid: str


class HealthzOkResponse(BaseModel):
    status: str = "ok"


class BindingObject(BaseModel):
    source_uid: str
    destination_uid: str


class BindingCreateRequest(BindingObject):
    pass


class Binding(BindingObject):
    uid: str


@app.get(
    "/time",
    response_model=int,
    description="Return current unix timestamp in milliseconds from server.",
)
async def time():
    """
    Get current time.
    """
    return 0


@app.get(
    "/healthz",
    response_model=HealthzOkResponse,
)
async def healthz():
    """
    Health check.
    """
    return HealthzOkResponse()


@app.post("/apis/v1/sources", response_model=Source)
async def create_source(source: SourceCreateRequest):
    """
    Create a source.
    """
    return Source()


@app.get("/apis/v1/sources", response_model=t.List[Source])
async def list_sources():
    """
    List all sources.
    """
    return [Source()]


@app.get("/apis/v1/sources/{source_uid}", response_model=Source)
async def get_source(source_uid: str):
    """
    Get a source.
    """
    return Source()


@app.delete("/apis/v1/sources/{source_uid}")
async def delete_source(source_uid: str):
    """
    Delete a source.
    """
    return "OK"


@app.post("/apis/v1/destinations", response_model=Destination)
async def create_destination(destination: DestinationCreateRequest):
    """
    Create a destination.
    """
    return Destination()


@app.get("/apis/v1/destinations", response_model=t.List[Destination])
async def list_destinations():
    return [Destination()]


@app.get("/apis/v1/destinations/{destination_uid}", response_model=Destination)
async def get_destination(destination_uid: str):
    return Destination()


@app.delete("/apis/v1/destinations/{destination_uid}")
async def delete_destination(destination_uid: str):
    return "OK"


@app.post("/apis/v1/source_groups", response_model=SourceGroup)
async def create_source_group(source_group: SourceGroupCreateRequest):
    """
    Create a source group.
    """
    return SourceGroup()


@app.get("/apis/v1/source_groups", response_model=t.List[SourceGroup])
async def list_source_groups():
    """
    List all source groups.
    """
    return [SourceGroup()]


@app.get("/apis/v1/source_groups/{source_group_uid}", response_model=SourceGroup)
async def get_source_group(source_group_uid: str):
    """
    Get a source group.
    """
    return SourceGroup()


@app.delete("/apis/v1/source_groups/{source_group_uid}")
async def delete_source_group(source_group_uid: str):
    """
    Delete a source group.
    """
    return "OK"


@app.get("/apis/v1/bindings", response_model=t.List[Binding])
async def list_bindings():
    """
    List all bindings.
    """
    return [Binding()]


@app.post("/apis/v1/bindings", response_model=Binding)
async def create_binding(binding: BindingCreateRequest):
    """
    Create a binding.
    """
    return Binding()


@app.get("/apis/v1/bindings/{binding_uid}", response_model=Binding)
async def get_binding(binding_uid: str):
    """
    Get a binding.
    """
    return Binding()


@app.delete("/apis/v1/bindings/{binding_uid}")
async def delete_binding(binding_uid: str):
    """
    Delete a binding.
    """
    return "OK"
