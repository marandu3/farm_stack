from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Path, Query
from typing import Union, Annotated
from .schemas import BandBase, BandWithID,BandCreate
from .schemas import GenreURLChoices


app= FastAPI()


BANDS = [
    {'id': 1, 'name': 'Band A', 'genre': 'Rock'},
    {'id': 2, 'name': 'Band B', 'genre': 'Pop'},
    {'id': 3, 'name': 'Band C', 'genre': 'Jazz', 'albums':[
        {'title': 'Album 1', 'release_date': '2022-01-01'}
    ]},
    {'id': 4, 'name': 'Band D', 'genre': 'Classical'},
    {'id': 5, 'name': 'Band E', 'genre': 'Hip-Hop'},
    {'id': 6, 'name': 'Band F', 'genre': 'Country'},
]


@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/bands')
async def get_bands(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=10)] = None,          
)->list[BandWithID]:
    
    band_list = [BandWithID(**band) for band in BANDS]
    print 
    
    if genre:
        band_list = [
            band for band in BANDS if band.genre.lower() == genre.value.lower()
        ]

    if q:
        band_list = [
            band for band in band_list if q.lower() in band.name.lower()
        ]

    return band_list

@app.get('/bands/{band_id}')
async def get_band(band_id:Annotated[int,Path(title="The band ID")]) -> BandWithID:
    band = next((BandWithID(**band) for band in BANDS if band['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found")
    return band

@app.get('/bands/genre/{genre}')
async def bands_by_genre(genre:str) -> list[dict]:
    bands = [bands for band in BANDS if band['genre'].lower() == genre.lower()]
    if not bands:
        raise HTTPException(status_code=404, detail="No bands found for this genre")
    return bands

@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id']+1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band
