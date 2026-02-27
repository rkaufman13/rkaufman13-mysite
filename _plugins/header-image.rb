require 'puppeteer-ruby'
require 'rickshaw'

module Jekyll
    class HeaderFilter < Liquid::Tag

        def initialize(tag_name, text, tokens)
            super
        end

        def render(context)
            #choose a random image from the opengraph folder and return it
            image_location = Dir.glob("/home/rachel/rkaufman13-mysite/assets/opengraph/*").sample
            image_location.sub! "/home/rachel/rkaufman13-mysite",""
            
        end
    end
end

Liquid::Template.register_tag('custom_header_image', Jekyll::HeaderFilter)