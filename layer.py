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


from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import \
    TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities import \
    OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities import \
    OutgoingAckProtocolEntity


class WhatsappTunnel(YowInterfaceLayer):

    """Whatsapp host of the tunnel."""

    @ProtocolEntityCallback("message")
    def onMessage(self, msgProtocolEntity):
        """Called when received a message."""
        rcp = OutgoingReceiptProtocolEntity(msgProtocolEntity.getId(),
                                            msgProtocolEntity.getFrom(),
                                            'read',
                                            msgProtocolEntity.getParticipant())

        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            msgProtocolEntity.getBody(),
            to=msgProtocolEntity.getFrom())

        print(msgProtocolEntity.getBody())
        print(msgProtocolEntity.getFrom())
        self.toLower(rcp)
        # self.toLower(outgoingMessageProtocolEntity)

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        """Called when received an ACK."""
        ack = OutgoingAckProtocolEntity(entity.getId(), 'receipt',
                                        entity.getType(), entity.getFrom())
        self.toLower(ack)
