require 'date'

module Jekyll
    class LastBuilt < Liquid::Tag

        def initialize(tag_name, text, tokens)
            super
            @text = text
        end

        def render(context)
             asdf
            #Time.now.strftime("%Y, %B %d")
        end
    end
    
end

Liquid::Template.register_tag('last_built', Jekyll::LastBuilt)