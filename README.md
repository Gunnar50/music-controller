# music-controller

## Prerequisites

- [GCloud](https://cloud.google.com/sdk/docs/install)
- [uv](https://github.com/astral-sh/uv)

## Install, Build and Deployment

### Local Development

Ensure all the pre-requisites are installed, then:
- Login to gcloud - `gcloud auth login` & `gcloud auth application-default login`
- Install the project Python versions - `uv python install`

## Views & APIs
Pages
Index - /
Create room - /create
Get Room - /<room_code>

Room APIs
Create a room - POST /api/room
Join a room - POST /api/room/<room_code>
Leave a room (owner deletes the room) - POST /api/room/<room_code>/leave
Update room - PUT /api/room/<room_code>
Get users in room - GET /api/room/<room_code>/users

Spotify APIs
Auth - POST /api/spotify/auth
Get current playing song - GET /api/spotify
Search song - POST /api/spotify/search
Add to queue - POST /api/spotify/queue
Vote to skip - POST /api/spotify/vote
Play song - POST /api/spotify/play
Pause song - POST /api/spotify/pause
Skip song - POST /api/spotify/skip
