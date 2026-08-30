---
layout: post
title: Fun With DNS TXT Records
categories: things-i-learned
excerpt_separator: <!--more-->
description: For some definitions of "fun"
---

![The famous DNS haiku on a background of cherry blossoms. "It's not DNS / There's no way it's DNS / it was DNS."](/assets/2026/dns.jpg)

I got back to work after a vacation and was immediately handed a small pile of tickets related to DNS.

For the purpose of this post, it doesn't actually matter what I'm doing with DNS, but it did mean I had to re-familiarize myself with a lot of concepts and learn about a few more.

The type of DNS record that I'm least familiar with, although also the simplest one, is probably TXT. I'm least familiar with it because it has tons of uses.

If you've done anything with DNS, you've likely seen TXT records used for things like:

- validating domain ownership
- setting up DKIM (DomainKeys Identified Mail) for helping with email delivery, or SPF records for same

It's the simplest because unlike other types of DNS records, the spec for TXT is....text. You can put anything in there. As long as it's 255 characters or less.

This poses a problem. Some TXT records, especially when we're talking about DKIM records, are very, very long. Some DNS providers are kind enough to accept a large string and split it behind the scenes, but others, such as AWS Route53, follows [the spec](https://www.rfc-editor.org/info/rfc1035/#section-2.3.4) to the letter. (Aside, if I'm reading this spec correctly, every DNS record, not just TXT, is capped at 255 characters, it's just that other types of records rarely if ever get that large). If you need to add a long TXT record to Route53 or other providers that follow the spec, you must manually split the record; the resolver handles concatenating the strings back together into a larger record.

So that was already kind of interesting. You can just split these strings, including a long public key right in the middle, and something magically figures out how to recreate the key? Cool.

Then I found [this blog post by Breanne Boland](https://breanneboland.com/blog/2020/02/28/you-can-put-what-in-dns-txt-records-a-blog-post-for-con-west-2020/) and I realized I'd not even scratched the surface.

You can put *anything* in txt records, it turns out. Boland cites the example of a university that put lat/long in each server's TXT records so people could find them, physically, on a giant campus. So far, so good.

[Jetbrains offers a way to discover license servers through TXT records](https://www.jetbrains.com/help/license_server/configure_automatic_server_discovery.html#configure-automatic-license-discovery). That's pretty cool. Okay, but...

Until 2024, you could get summaries of any Wikipedia article you wanted [through DNS](https://dgl.cx/2008/10/wikipedia-summary-dns), thanks to this incredible project by David Leadbeater; this project is no longer available but [Wordle over DNS](https://dgl.cx/2022/02/wordle-over-dns) (also by David) works.

This madman [stored a blog post in TXT records](https://blog.benjojo.co.uk/post/dns-filesystem-true-cloud-storage-dnsfs) (don't do this).

Some people just include [jokes](https://search.reconwave.com/show/domain/dimme.net). There's a whole choose-your-own-adventure stored in TXT records: just `dig TXT 1.adventure.splode.com`.

It's not all fun and games. In 2025,[hackers used TXT records to distribute malware](https://www.activecountermeasures.com/malware-of-the-day-txt-record-abuse-in-dns-c2-joker-screenmate/).

Obgliatory mention: You can play around with DNS at [messwithDNS.net](https://messwithdns.net/) which I strongly recommend.
