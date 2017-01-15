"""
Vimeo Tag
---------
This implements a Liquid-style vimeo tag for Pelican,
based on the youtube tag which is in turn based on
the jekyll / octopress youtube tag [1]_

Syntax
------
{% vimeo id %}

Example
-------
{% vimeo 10739054 %}

Output
------
<span style="width:640px; height:480px;">
    <iframe
        src="//player.vimeo.com/video/10739054?title=0&amp;byline=0&amp;portrait=0"
        width="640" height="480" frameborder="0"
        webkitallowfullscreen mozallowfullscreen allowfullscreen>
    </iframe>
</span>

[1] https://gist.github.com/jamieowen/2063748
"""
import re
from .mdx_liquid_tags import LiquidTags

SYNTAX = "{% vimeo id %}"

VIMEO = re.compile(r'(\S+)?')


@LiquidTags.register('vimeo')
def vimeo(preprocessor, tag, markup):
    vimeo_id = None

    match = VIMEO.search(markup)
    if match:
        groups = match.groups()
        vimeo_id = groups[0]

    if vimeo_id:
        vimeo_out = """
            <div class="embed-responsive embed-responsive-16by9">
                <iframe 
                    class="embed-responsive-item" 
                    src="//player.vimeo.com/video/{vimeo_id}?title=0&amp;byline=0&amp;portrait=0" 
                    webkitAllowFullScreen mozallowfullscreen
                    allowFullScreen>
                </iframe>
            </div>
           
        """.format(vimeo_id=vimeo_id).strip()
    else:
        raise ValueError("Error processing input, "
                         "expected syntax: {0}".format(SYNTAX))

    return vimeo_out


# ---------------------------------------------------
# This import allows vimeo tag to be a Pelican plugin
from liquid_tags import register  # noqa
