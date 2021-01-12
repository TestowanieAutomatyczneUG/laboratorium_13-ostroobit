from behave import *

def before_scenario(context, scenario):
    print("Message before scenario")

def after_scenario(context, scenario):
    print("Message after scenario")