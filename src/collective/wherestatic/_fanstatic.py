from fanstatic import NeededResources

MARK = '<!-- #RESOURCES -->'

class CustomNeededResources(NeededResources):
    """Replaces render_* methods so that resources get
    inserted at the marked point.

    """
    
    def render_into_html(self, html):
        """Render needed resource inclusions into HTML.

        :param html: A string with HTML to render the resource
          inclusions into. This string must have a
          ``<!-- #RESOURCES -->`` section.

        """

        to_insert = self.render()
        return html.replace(MARK, to_insert, 1)

    def render_topbottom_into_html(self, html):
        top, bottom = self.render_topbottom()
        if top:
            html = html.replace(MARK, top, 1)
        if bottom:
            html = html.replace('</body>', '%s</body>' % bottom, 1)
        return html
