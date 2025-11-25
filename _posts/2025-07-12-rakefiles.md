---
layout: post
title: "Some Basic Rake Tasks for Jekyll Users"
categories: things-i-learned
excerpt_separator: <!--more-->
description: Anyone with a Jekyll blog is welcome to these.
tags: jekyll
image: /assets/zen-garden.jpg
---

![An image of a zen sand garden being raked.](/assets/zen-garden.jpg)

I recently tweaked a few of the (very basic) rake tasks I'm using to keep this blog going. Ruby isn't my thing, but writing these was interesting and I figured I'd share in case they are useful to anyone else.

### Wait, back up. What's a rake task?

Rake is a task runner in Ruby. Jekyll, which powers this blog, is written in Ruby. Similar to how a JS-based project might have scripts in `package.json` that allow a developer to run tests or start a server, rake allows devs to define custom tasks and then run them, using the syntax `rake taskname`. In my case, I wanted a task that would create a new draft based on a template, and a task that would automate deployment of the blog, to prevent any mistakes from making it into prod. (I recently erased my site by `rsync`ing the wrong directory to my server. I got it back a minute later, but I'm tired of doing that.)

### Ok, I'm sold. How do I write a rake task?

I created a file in my site's root directory called `rakefile` that holds the tasks. Then I define my tasks in Ruby. I had to google a lot of syntax for these very basic tasks -- Ruby is not a language I know!

```ruby
desc "Create draft with template."

task :newdraft do
  puts "new draft name: "
  my_file = STDIN.gets.chomp
  source_file = "path/to/site/root/folder/template.md"
  destination_file = "path/to/site/root/folder/_drafts/#{my_file}.md"
  unless File.exist?(destination_file)
    FileUtils.cp(source_file,destination_file)
    puts destination_file
  end
  cmd = "code #{destination_file}"
  system(cmd)
end
```

This defines a task that takes input from the user (me), and creates a new Markdown file from copying a basic template with some default front-matter defined, then opens it in VSCode. Notice I have basically no input sanitization here, and things like the default IDE (VSCode) are hardcoded. Change to suit your needs.

The other thing you'll notice is that the task has a description. This, it turns out, is required for the task to be discoverable by Ruby, so don't leave it out!

The second task is even simpler:

```ruby
desc "Build and deploy."
task :deploy do
    system("/path/to/deploy/script.sh")
end
```

The deploy script is a simple bash script that changes to the site's root directory, runs the jekyll build command, then rsyncs the `_site` folder to another folder on my computer, which is set up with Syncthing to copy new files to the remote web server. (This is not a typical build pipeline and I am thankful to be in a two-nerd household.)

One might ask, why have a rake task if all it does is execute a shell script? The cool thing about rake tasks is they can be executed from anywhere in the directory tree at the level of the rakefile or below. As I understand it, `rake` will start in its current directory and then keep going upward until it finds a rakefile with a matching task name. 

This is why 'real' Ruby projects usually [namespace](https://stackoverflow.com/questions/50673888/rake-task-and-namespaces) their tasks, because this behavior in a big project could lead to issues. In my tiny project, though, it's exactly what I want. Now, I can do `rake deploy` from anywhere within my site structure.

Yes, I could also just run `/the/full/path/to/deploy.sh` from anywhere, but that involves more typing.

That got me thinking, too -- to start the Jekyll local server, I type `bundle exec jekyll serve --drafts`. This can be shortened to `bundle exec jekyll s -D`, and if I use history search it's really not that bad to retrieve this command, but could I make this more efficent?

With a rake task that looks like this:

```ruby
task :start, :withDrafts do |t, args| 
  trap('SIGINT') { puts "\nI quit."; exit }
  args.with_defaults(:withDrafts=>"false")
  puts("Running the server with drafts #{args[:withDrafts]? 'on': 'off'}")
  system '/path/to/start/file/start.sh', args[:withDrafts]
end
```

and a bash script that looks like this:

```bash
#! /bin/bash

SITE_ROOT_DIR="/full/path/to/my/site/root"
WITH_DRAFTS=$1
if [ $WITH_DRAFTS = 'true' ]; then
    cd $SITE_ROOT_DIR && bundle exec jekyll serve --drafts
else
    cd $SITE_ROOT_DIR && bundle exec jekyll serve
fi
```

I can start a rake task that starts the server and waits until I ctrl-c to end the task. There are two somewhat interesting bits in the Ruby code: `trap` works the same as a `bash` trap, in that it listens for the ctrl-c signal and then executes the code in the function. This is just to make the exit look cleaner, the task works fine without it.

And adding the `:withDrafts` parameter to the task, with a default set of false, allows me to pass true or false into the shell script. This syntax is pretty bonkers to me as a non-Ruby user but it seems to work fine.

Note that for both of the tasks that run shell scripts, `chmod +x script.sh` is required to make Ruby able to run these as executables.

This was a fun exercise. I have now written nearly 900 words on this topic, plus the testing and writing of the rake file itself, which means I have not yet saved myself any time with these new commands. But maybe a hundred or so blog posts later I'll be singing a different tune. :)