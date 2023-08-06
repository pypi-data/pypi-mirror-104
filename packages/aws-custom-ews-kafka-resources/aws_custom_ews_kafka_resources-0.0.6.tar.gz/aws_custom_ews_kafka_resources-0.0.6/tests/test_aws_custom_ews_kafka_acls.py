#!/usr/bin/env python

"""Tests for `aws_custom_ews_kafka_resources` package."""

from pytest import raises
from troposphere import Template

from aws_custom_ews_kafka_resources import KafkaAclPolicy
from aws_custom_ews_kafka_resources import resource
from aws_custom_ews_kafka_resources import custom


def test_kafka_rtopics():
    """
    Function to test normal working of the
    :return:
    """
    template = Template()
    r_topic = resource.KafkaAcl(
        "ACL01",
        BootstrapServers="broker.cluster.internal",
        Policies=[
            KafkaAclPolicy(
                Resource="Topic01",
                ResourceType="TOPIC",
                Host="*",
                Principal="User:1234",
                Action="READ",
                Effect="ALLOW",
            )
        ],
    )
    template.add_resource(r_topic)
    template.to_json()


def test_kafka_ctopics():
    template = Template()
    c_topic = custom.KafkaAcl(
        "newtopiccustom",
        ServiceToken="arn:aws:lambda:eu-west-1:012345678912:function:name",
        BootstrapServers="broker.cluster.internal",
        Policies=[
            KafkaAclPolicy(
                Resource="Topic01",
                ResourceType="TOPIC",
                Host="*",
                Principal="User:1234",
                Action="READ",
                Effect="ALLOW",
            )
        ],
    )
    template.add_resource(c_topic)
    template.to_json()
