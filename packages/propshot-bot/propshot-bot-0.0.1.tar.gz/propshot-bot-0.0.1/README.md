# propshot-bot
snap[shot]+(prop)osal-bot = (prop)[shot]-bot

A discord bot package to monitor and alert about [snapshot](https://snapshot.org) proposals. 

## Prerequisites
Get a discord bot/user account token. [Step through of getting a bot token.](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token)
The bot must have permission to send messages on the desired channel.


## Build

### Using the docker-compose.yml.template
 - `cp docker-compose.yml.template docker-compose.yml`
 - `docker-compose build`
 - The built image name is `propshot-bot:latest`.
 - Then set environmetnal vars (specified below) and run the image `docker-compose up -d`

## Install
### Pip
    `pip install propshot-bot`
    

## Configuration
Required:
 - `DISCORD_BOT_TOKEN`
 - `DISCORD_OUTPUT_CHANNEL`
 - `SPACES`
Optional:
 - `alert_thresholds` := A list of 2-tuples. The 2-tuples is expected to be an integer representing seconds and then a hexidecimal number to describe a color. The list is expected to be in ascending based on the seconds. 
 - `CHECK_FREQUENCY`

### Environment Vars
 - `SPACES` := snapshot proposals space separated list.
 - `DISCORD_BOT_TOKEN` := discord bot token ( [discord developer page] (https://discord.com/developers/applications]) > specific application > bot tab > token > reveal)
 - `DISCORD_OUTPUT_CHANNEL` := string of discord channel name (channels with emojis not tested)
 - `PERSISTENT_LOCATION` := file path to keep stateful information for proposals between restarts
 - `CHECK_FREQUENCY` :=  seconds between new proposals fetch. Default is 300 seconds aka 5 minutes.
 
> Providing `PERSISTENT_LOCATION` will not resend alerts for already known active proposals when bot is restarted. This way the bot may be start and stopped without spamming alerts. 
 


## Usage 
It is recommened to configure the bot through environment variables. Environment variables makes deploying the bot with docker containers easy. If the user's wish is to deploy a bot with the sole purpose of this package, the user may find using the image on dockerhub easier. 
It is recommended to deploy using the docker image. qIf the user's wish is to add this into an existing bot, use `pip install propshot-bot`. 
If you wish to just import the package (example assumes required variables from above are set as env vars)
```
import discord
import os
from proposals.proposal_discord import ProposalMonitorDiscord

client = discord.Client()
snapshot = ProposalMonitorDiscord(client)
client.run(os.getenv('DISCORD_BOT_TOKEN'))
```


### Docker 
If you wish to use the docker to deplo the bot, 
```
docker pull fuzzylemma/propshot-bot:latest
docker run -dp 443:443 \
  --env SPACES=$SPACES \
  --env DISCORD_BOT_TOKEN=$DISCORD_BOT_TOKEN \
  --env DISCORD_OUTPUT_CHANNEL=$DISCORD_OUTPUT_CHANNEL \
  --env PERSISTENT_LOCATION=$PERSISTENT_LOCATION \
  --mount type=bind,souce="${SOMEWHERE_ON_HOST},target=$PERSISTENT_LOCATION \
  fuzzylemma/propshot-bot:latest
```
This assumes the env vars are assigned on the host. Feel free to replace variable with desired values.  
If the image was built locally, replace the dockerhub image name with your local image name. 