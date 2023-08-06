Advanced Usage
==============

Dynamic Group Naming
--------------------

Sometimes a group can't be named ahead of time and needs to be named
dynamically based on some other input. A good example of this might be
because the group is related to a given class which may be subclassed
and its name needs to be unique at time of registration rather than
unique at time of definition.

A DynamicNameConfigGroup looks almost like a normal group, but it needs
to have the name set before being registered or it will raise an error::

    # ./my_app/plugins/dynamic_plugin.py
    from confspirator import groups, fields

    class SomePluginClass(object):

        config_group = groups.DynamicNameConfigGroup(
            description="A dynamicly named sub group under the root group.",
            children=[
                fields.BoolConfig(
                    "bool_value",
                    help_text="some boolean flag value",
                    default=True,
                ),
            ]
        )

    # ./my_app/plugins/loading.py
    from my_app.config import root

    def setup_plugin_config(plugin_class):
        config_copy = plugin_class.config_group.copy()
        config_copy.set_name(plugin_class.__class__.__name__)
        root.root_group.plugins_group.register_child_config(config_copy)

In the above example we are also first making a copy of the group so that
we don't set a name on the group associated with the plugin class. The new
copy will be a deep copy, and will include any subgroups if there are any.

Extending Existing Groups
-------------------------

Sometimes you would like to reuse and extend an existing config group.
In those cases the extend function will allow you to make a deep copy
of another config group, and add additional children to it (either fields
or further sub-groups).

The original reason for this feature was for extending class associated config
and being able to inherit the parent config as a base starting point::

    # ./my_app/plugins/dynamic_plugin.py
    from confspirator import groups, fields

    class SomeOtherPluginClass(SomePluginClass):

        config_group = SomePluginClass.config_group.extend(
            children=[
                fields.StrConfig(
                    "my_string_config",
                    help_text="Some useful help text.",
                    required=True,
                    default="stuff",
                ),
            ]
        )

This could also be used outside of class contexts when building generic
config groups as a base for other elements of your app, and having specific
groups extend the base one for the extra parts they need. It helps minimise
duplication if used right.

.. note::

    When extending you can also pass a list of strings to the `remove_children`
    function parameter to have the keys given removed from the children of the
    group.

Overlaying Groups
-----------------

Loaded config groups have the ability to have another group or a dictionary
overlaid on top of them, with the returned object being a deep copy of the
target overlaid by the given group or dictionary.

This is essentially a depth first dictionary update, where only keys in the
given group or dictionary will be overridden inside the target group.

It can be as simple as just merging two groups together::

    merged_config = CONF.plugins.defaults.overlay(
        CONF.plugins.SpecificPlugin)

But this is most effective when the configs are designed to be overlaid cleanly
for the purposes of overriding defaults, or some other scenario where a base
config group needs some of its values overridden by config defined elsewhere.

The original use case for this feature was to allow defining a default for all
instances of a given class, and having an easy way to overlay more specific
config on top of the defaults for different places that class was used, to have
that config passed down to the code that needed it in the most specific state::

    def get_action_config(action_name, task_type):
        try:
            action_defaults = CONF.workflow.action_defaults.get(action_name)
        except KeyError:
            return {}

        try:
            task_conf = CONF.workflow.tasks[task_type]
            return action_defaults.overlay(task_conf.actions[action_name])
        except KeyError:
            return action_defaults

Lazy Loading Groups
-------------------

In rather weird cases where plugins or application startup may register
more configuration that can't be parsed right away, you can make a group
lazy load itself when first accessed.

This might be useful where one part of your config will define what plugins
are enabled, or needed to start the application at all, but during that start
up or loading process more configs will be registered.

Having a group be lazy loaded is as simple as setting a parameter when making
the group::

    lazy_loaded_group = groups.ConfigGroup("lazy_loaded", lazy_load=True)

Any fields or subgroups registered to this group before it is first access via
the loaded config will be included in the loaded config. Up until first access
the loaded group namespace retains a link back to the group definition, the
loaded config file, and environment variables, which are processed on first
access into a fully loaded group namespace.
