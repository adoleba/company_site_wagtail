from django import template

register = template.Library()


@register.simple_tag
def block_value(blocks, block_type):
    for block in blocks:
        if block.block_type == block_type:
            return block.value
