from datetime import datetime

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.db import get_db

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def view_items(request: Request, db: AsyncSession = Depends(get_db)):
    items = await db.execute(
        select(
            models.DemoTable.id,
            models.DemoTable.created_at,
            models.DemoTable.updated_at,
            models.DemoTable.value,
        ).order_by(models.DemoTable.id)
    )
    return templates.TemplateResponse(
        "index.html", {"request": request, "items": items.all()}
    )


@app.post("/add")
async def add_item(value: str = Form(...), db: AsyncSession = Depends(get_db)):
    item = models.DemoTable(value=value)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return RedirectResponse(url="/", status_code=303)
