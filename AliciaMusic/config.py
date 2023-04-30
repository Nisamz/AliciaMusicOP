# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith 

from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BABdctkRvIomq5EhjFUgy7hFJo_PgGoBhNJDXkxhA301Uz65ETq2UHAlSADwjzppbD2wv3zzEcIj6a6Ce2WykPRNQgPK6jFQINzM9yEVl5ZqxLpTAd5crIb07aRl8MYqZXAsb4h1J7Kdtfc69MVYny0w6_UaMYlnhePXIPwUnnOfcnjh80PlHx-3LSLgN2xrHACL2otUXNzbYKBfVfY7ON_AS_DxmGAb0J09rIJdudGpYsz4qjbkOpIkZNUwL1_92Uuv6sji3xHxin0j4mrbWaYSzOt8Uxs4QiAUUzRbWcI1gIU3LSe8_wTPR9L_NggZ6ZW7-AOtOuATZQrLKKUE5wHzAAAAAXLR6oYA")
BOT_TOKEN = getenv("BOT_TOKEN", "6064828747:AAGGsd9LZFldfGHCQwtGglOjZ5eHH-giDb8")
BOT_NAME = getenv("BOT_NAME", "𝐀𝐥𝐢𝐜𝐢𝐚 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸")
BOT_USERNAME = getenv("BOT_USERNAME", "renamexzsaew_bot")
BOT_PIC = getenv("BOT_PIC", "https://graph.org/file/2908f0618437ce1d06970.jpg")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "treasmno")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Bssam_fsr4")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "cxzsaewm")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Bssam_fsr4")
admins = {}
API_ID = int(getenv("API_ID", "25956685"))
API_HASH = getenv("API_HASH", "782885f0fc9c7f1824841916ec4787c5")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
ARQ_API_KEY = getenv("ARQ_API_KEY")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
