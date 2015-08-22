"""Telewhat-Tunnel."""
# Copyright (C) 2015 Benito Palacios Sánchez <benito356@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from yowsup.layers import YowLayer
from yowsup.layers.protocol_messages.protocolentities import \
    TextMessageProtocolEntity


class WhatsappLayer(YowLayer):

    """Application Whatsapp Layer."""

    def receive(self, protocolEntity):
        """Called when received a packet."""
        if protocolEntity.getTag() == "message":
            self.onMessage(protocolEntity)

    def onMessage(self, messageProtocolEntity):
        """Called when received a message."""
        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            messageProtocolEntity.getBody(),
            to=messageProtocolEntity.getFrom())

        self.toLower(outgoingMessageProtocolEntity)
