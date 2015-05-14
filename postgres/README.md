## For boot2docker on MAC
run `$(boot2docker shellinit 2> /dev/null)`
Also put `$(boot2docker shellinit 2> /dev/null)` the bottom of your `~/.bash_profile`

## For persistent data
`mkdir <some_place_to_store_data`

docker run --name gtoken-postgres [-e POSTGRES_PASSWORD=mysecretpassword] [-v <some_place_to_store_data>:/var/lib/postgresql] -d postgres
