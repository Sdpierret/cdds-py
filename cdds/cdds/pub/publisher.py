from cdds.core import Entity
from cdds.domain.participant import DomainParticipant
from cdds.internal import c_call, dds_entity_t, dds_qos_p_t, dds_listener_p_t


class Publisher(Entity):
    def __init__(self, domain_participant: DomainParticipant, qos=None, listener=None):
        self.domain_participant = domain_participant
        self.qos = qos
        self.listener = listener
        
        self._ref = self._create_publisher(domain_participant._ref, qos, listener)

    @c_call("dds_create_publisher")
    def _create_publisher(self, domain_participant: dds_entity_t, qos: dds_qos_p_t, listener: dds_listener_p_t) -> dds_entity_t:
        pass

