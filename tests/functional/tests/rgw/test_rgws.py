import pytest


class TestRGWs(object):

    @pytest.mark.no_docker
    def test_ceph_rgw_package_is_installed(self, node, Package):
        assert Package("radosgw").is_installed


    def test_rgw_services_are_running(self, node, Service):
        # TODO: figure out way to paramaterize node['rgws'] for this test
        for rgw in node["rgws"]:
            assert Service("ceph-radosgw@%s" % rgw).is_running

    def test_rgw_services_are_enabled(self, node, Service):
        # TODO: figure out way to paramaterize node['rgws'] for this test
        for rgw in node["rgws"]:
            assert Service("ceph-radosgw@%s" % rgw).is_enabled
