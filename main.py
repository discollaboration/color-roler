from speedcord import Client
from speedcord.http import Route
from os import environ as env
from random import choice

client = Client(2)
client.current_shard_count = 1  # Hacky fix until its fixed
client.token = env["TOKEN"]

roles = env["ROLES"].split(";")


@client.listen("GUILD_MEMBER_ADD")
async def on_member_join(data, _):
    user_id = data["user"]["id"]
    guild_id = data["guild_id"]
    route = Route("PUT", "/guilds/{guild_id}/members/{user_id}/roles/{role_id}",
                  guild_id=guild_id,
                  user_id=user_id,
                  role_id=choice(roles)
                  )
    await client.http.request(route)


client.run()
