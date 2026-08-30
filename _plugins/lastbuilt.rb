require 'date'

module Jekyll
    class LastBuilt < Liquid::Tag

        def initialize(tag_name, text, tokens)
            super
            @text = text
        end

        def render(context)
             Time.now.strftime("%B %d, %Y")
        end
    end
    
end

Liquid::Template.register_tag('last_built', Jekyll::LastBuilt)