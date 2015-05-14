## For boot2docker on MAC
run `$(boot2docker shellinit 2> /dev/null)`

Also put `$(boot2docker shellinit 2> /dev/null)` the bottom of your `~/.bash_profile`

## For persistent data
`mkdir <some_place_to_store_data>`

## Commands

To bring docker postgres up from scratch
`docker run --name gtoken-postgres [-e POSTGRES_PASSWORD=mysecretpassword] [-v <some_place_to_store_data>:/var/lib/postgresql] -d postgres`

To stop docker postgres
`docker stop gtoken-postgres`

To bring a stopped docker back
`docker start gtoken-postgres`

Avoid removing docker postgres if possible, because it would **erase all data**
`docker rm gtoken-postgres`
