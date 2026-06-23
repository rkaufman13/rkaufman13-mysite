---
layout: post
title: "30 Days of coreutils: chmod"
categories: things-i-learned
tags: coreutils bash cli
excerpt_separator: <!--more-->
project: "30 Days of Coreutils"
description: A deep dive into a "boring" utility.
---

{%include coreutils-header.html util="chmod" %}

So far this month, I've tried to write about utils in the coreutils collection that have something surprising or interesting about them, and to me `chmod`, which stands for "change mode," is not  what you would call interesting. But it's one that comes up a lot. If we are copying code from one of the Stack sites or elsewhere, often `chmod` is part of the mix, and so we may as well know what we are doing.

"Change mode" isn't a very descriptive way to explain what `chmod` does. In short, it determines who is allowed to access files, and what those people can do with them.

```bash
$ ls -l
-rw-rw-r-- 1 rachel rachel    20 May 18 13:35 file1.txt
```

See that incantation in the first column? The `-rw-rw-r--`? That lists a file's ownership and permissions, in order of:

- user
- group
- all others

It says that the owner of the file (`rachel`) can read and write it, other members of the file's group (also `rachel`) can read and write it, and users who are neither `rachel` nor in the `rachel` group can read the file, but not make changes to it. And no person can execute the file (which in this case makes sense as a `.txt` file should not contain executable content. )

Let's create a function and put it in `/usr/local/bin` and see what happens.

```bash
$ echo "echo $(whoami)" > dontyouknowwhoiam
$ sudo mv dontyouknowwhoiam /usr/local/bin
$ sudo dontyouknowwhoiam #this will fail because the file is not executable
sudo: dontyouknowwhoiam: command not found #the script is in my $PATH, but isn't executable! Proof:
$ ls -l /usr/local/bin/dont*
-rw-rw-r-- 1 rachel rachel 12 May 25 14:13 /usr/local/bin/dontyouknowwhoiam
$ sudo chmod +x /usr/local/bin/dontyouknowwhoiam #this makes the script executable. Proof: 
$ ls -l /usr/local/bin/dont*
-rwxrwxr-x 1 rachel rachel 12 May 25 14:13 /usr/local/bin/dontyouknowwhoiam
$ dontyouknowwhoiam # this will succeed!
rachel
```

Phew - that's a long example to show that `chmod +x` takes a file that is not executable, and makes it executable - by the owner, the group, and everyone else. I could have done `chmod u+x` to make it executable by only the file's owner, or `g+x` to add permissions to the file's group, etc. You can also use the minus sign to remove a permission, or `=` to set exact permissions (e.g. `chmod u=rwx myfile`). The equals sign can also be used to copy permissions from one user class to another, e.g. `chmod u=g` means, "the user should be assigned the permissions belonging to the group."

`chmod` also takes octal notation. I struggle to explain what this means in a succinct way, but imagine that each class of person (user, group, all) is a digit, and each digit can be a number from 0-8. Exec is represented by 1,  write is represented by 2, and read is represented by 4. By adding the numbers together, you get a set of permissions for each class; 7 means "read, write and execute" (because 4+2+1=7), 3 means "write and execute" (because 2+1=3), 6 means "read and write" (because 4+2=6) and so on. So `chmod 755 file`, which we see often, means "make the file readable and executable by everyone, as well as writable by the file's owner".

`chmod 777` is an interesting exception. It means to make a file accessible for all actions by everybody. To be clear you should not do this. You should absolutely not do `chmod -R 777` from the root of your file system. This breaks a lot of things. `ssh` famously will stop working because it assumes that Something Has Gone Terribly Wrong. See [this](https://superuser.com/questions/784973/i-broke-ssh-by-using-chmod-on-an-ec2-instance-how-do-i-correct) horror story from a while back.

Okay, I guess chmod is a bit more surprising than I thought!