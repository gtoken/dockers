## For boot2docker on MAC
run `$(boot2docker shellinit 2> /dev/null)`

Also put `$(boot2docker shellinit 2> /dev/null)` the bottom of your `~/.bash_profile`


## Commands

To bring docker mysql up from scratch
`docker run --name gtoken-mysql 
           -e MYSQL_ALLOW_EMPTY_PASSWORD=true 
           -d mysql`
           
To stop docker mysql
`docker stop gtoken-mysql`

To bring a stopped docker back
`docker start gtoken-mysql`

Avoid removing docker mysql if possible, because it would **erase all data**
`docker rm gtoken-mysql`
