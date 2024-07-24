---
layout: post
title: "Learnin' Kubernetes"
categories: things-i-learned
excerpt_separator: <!--more-->
---

![A Greek trireme, steered by a helmsman..get it?](/assets/trireme.jpg)

At work, all teams are being asked to adopt [Karpenter](https://karpenter.sh/), which, as you can tell from the name, is related to Kubernetes.

The adoption is a relatively simple process, thanks to pre-work other teams have done to automate most of the hard stuff. Realistically, I should just have to change a few values in a couple YAML files and be done with it. However, when you're talking about modifying deployed services, it always pays to be careful.

I felt like what I was being asked to do would be relatively simple if I only understood some of the terminology being used. I mean:

> Identify taints to add to provisioned nodes. If a pod doesn’t have a matching toleration for the taint, the effect set by the taint occurs (NoSchedule, PreferNoSchedule, or NoExecute).

Yikes?

So some basic terminology larnin' is in order. I'm not really a devops girl so I am starting with the true basics. Here are some of my notes. Any mistakes here, however, are fully my own.

_Note: I dithered for four days about whether to post this, but then I read [Comfortable with the struggle](https://rachsmith.com/comfortable-with-the-struggle/) and was reminded that not understanding things is the default mode for software developers. It's okay that I couldn't tell you the difference between a Kubernetes pod and a node until this week, although I feel better now that I have learned to tell them apart._

### Kubernetes

As explained by its [docs](https://kubernetes.io/), Kubernetes is an "open source system for automating deployment, scaling, and management of containerized applications." In other words, it manages your apps running in containers: with Kubernetes, you can easily scale an app up or down (increase or decrease the number of pods running your app), handle load balancing, and (for example) automatically reboot a pod if it is failing.

Fun fact because I am a language nerd: Kubernetes comes from _kybernetes_, the Greek word for "helmsman" (the idea being that if a Docker container is like a shipping container, then the helmsman is the person who steers all those containers around). Know what else can claim _kybernetes_ as a root word? If you guessed cybernetics, you'd be correct: Norbert Wiener claimed he coined the term because he was interested in systems of feedback, and said that ships' steering engines were "one of the earliest and best-developed forms of feedback mechanisms." ("Governor" is also derived from _kybernetes_ via Latin. Now that's cool.)

### Karpenter

An add-on for Kubernetes. Its value proposition is "just-in-time nodes." It is aimed at helping users reduce costs by auto-scaling-down nodes if they are underutilized, or switching to "spot instances" (an AWS product that basically runs your app on 'spare' computers), among other things.

### Pods / nodes / clusters

A pod is the smallest possible "unit" in Kubernetes - one container, for example. (However, a pod can hold more than one container (: ) A _node_ is the thing that the pods run on, typically a physical server or a virtual machine. All pods need a node to run on, but not all nodes have pods scheduled to them. A _cluster_ is a group of nodes. Typically a service would have a cluster per deploy environment, so one for dev, one for staging, etc. The Kubernetes _control plane_ lives at the cluster level.

### Control plane

Just a fancy name for the software that actually orchestrates the containers. The _scheduler_ is an important part of the control plane as it is the software that assigns pods to nodes. It can do this automatically, applying some sensible defaults, but if you work on a big production app you probably want more granular control, hence the next set of terms.

### Node affinity

Pods have what's called `node affinities` which means that they either want to run on a certain node (or a type of a node or a node location), or don't want to run on a certain node. For example, you might want two services that communicate with each other to be in the same geographic region, to reduce latency. It's all still electrons, after all. Or, you might want certain pods to only run on nodes with some minimum CPU power, or you might just want to make sure that your app is evenly spread across regions to better protect it from downtime.

### Taint

`Taint` is like the opposite of a node affinity, it says "don't put this pod on this node." Unless the node can _tolerate_ the taint...

### Toleration

A pod that has a _toleration_ matching a node's taint can still be scheduled on that node.

The syntax for taints and tolerations (in addition to all the new terminology) confused me.

This is the command to apply a taint to a node:

`kubectl taint nodes node1 key1=value1:NoSchedule`

This means that no pods can be _scheduled_ on (assigned to) a node _unless_ they have a toleration matching `key1=value1`. (I had assumed that this means no pods can be scheduled on that node _if_ their key/value matches, but it is the opposite.)

So now that we know (or at least have familiarized ourselves) with this terminology, we can go back to the Karpenter documentation from before:

> Identify taints to add to provisioned nodes. If a pod doesn’t have a matching toleration for the taint, the effect set by the taint occurs (NoSchedule, PreferNoSchedule, or NoExecute).

This just means Karpenter can control how nodes are tainted, rather than controlling it through K8s.

In the end, to adopt Karpenter on my service at work, it truly was a pretty easy lift; as I said, other teams did most of the hard work so I just had to update some YAML to tell Karpenter my service's tolerations and taints. For now, the taint is essentially, "don't run any pods on this node that don't belong to my team" and the toleration is "I belong to Rachel's team," so it's not too complicated. But now that it's set up we can (possibly) come up with some more interesting customizations in the future.

#### Resources

- [Karpenter explained with bouncy balls](https://www.youtube.com/watch?v=3QsVRHVdOnM)