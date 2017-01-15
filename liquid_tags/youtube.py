"""
Youtube Tag
---------
This implements a Liquid-style youtube tag for Pelican,
based on the jekyll / octopress youtube tag [1]_

Syntax
------
{% youtube id [aspect] %}

Example
-------
{% youtube dQw4w9WgXcQ [16by9|4by4] %}


[1] https://gist.github.com/jamieowen/2063748
"""
import re
from .mdx_liquid_tags import LiquidTags

SYNTAX = "{% youtube id [aspect_ratio] %}"

YOUTUBE = re.compile(r'([\S]+)(\s+([\S]+))?')


@LiquidTags.register('youtube')
def youtube(preprocessor, tag, markup):
    aspect_ratio = '16by9'
    youtube_id = None

    match = YOUTUBE.search(markup)
    if match:
        groups = match.groups()
        youtube_id = groups[0]
        aspect_ratio = groups[2] or aspect_ratio

    if youtube_id:
        youtube_out = """
            <div class="embed-responsive embed-responsive-{aspect_ratio}">
                <iframe 
                    class="embed-responsive-item" 
                    src="//www.youtube.com/embed/{youtube_id}" 
                    webkitAllowFullScreen mozallowfullscreen
                    allowFullScreen>
                </iframe>
            </div>
        """.format(aspect_ratio=aspect_ratio, youtube_id=youtube_id).strip()
    else:
        raise ValueError("Error processing input, "
                         "expected syntax: {0}".format(SYNTAX))

    return youtube_out


# ---------------------------------------------------
# This import allows image tag to be a Pelican plugin
from liquid_tags import register  # noqa
