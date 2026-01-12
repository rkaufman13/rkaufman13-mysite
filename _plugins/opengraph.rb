require 'puppeteer-ruby'
require 'rickshaw'

module Jekyll
    class OGFilter < Liquid::Tag

        def initialize(tag_name, text, tokens)
            super
            @text = text
        end

        def render(context)
            if (context["page"]["path"]).include?"_posts/" and (context["page"]["layout"])=="post"
                # Create the image id from the page title in Jekyll
              id = context["page"]["path"].byteslice(7..-4)
         # Check if the file already exists in the 'opengraph' foldler, return early if it does
            
            unless (File.exist?("#{Dir.pwd}/assets/opengraph/#{id}.png")) 
               Puppeteer.launch(headless: true) do |browser|
               page = browser.new_page
               page.goto("file:///home/rachel/rkaufman13-mysite/truchet.html?foo=#{context["page"]["title"]}")
               page.screenshot(path: "#{Dir.pwd}/assets/opengraph/#{id}.png", type:"png",clip: {x:10,y:10, width:1190, height:630})
               
            end
        end  
            "/assets/opengraph/#{id}.png"
            
        
        end
    end
    end
end

Liquid::Template.register_tag('og_filter', Jekyll::OGFilter)