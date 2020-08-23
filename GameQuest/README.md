# Some thoughts
The game we made is extremely simplistic, yet we wrote nearly 500 lines of code to make it work (and just barely work, at that).

Why is this? Why did I make you write hundreds of lines of boring class definitions for something so simple that it could be accomplished with maybe 200 lines of top-level code? Why does it seem that half of the words you typed were "self"?

The reason, I'll tell you, is *design*.

Let me give you a taste what the "official" curriculum for this class consists of, using their shoot function as an example:

```
player_can_shoot = True
kills = 0
def shoot(x, y):
  global ammo_left
  global kills
  global player_can_shoot
  
  if ammo_left > 0 and player_can_shoot:
  
    player_can_shoot = False  # LOCK SHOOTING
    bullet.penup()
    bullet.setpos(*player.pos())
    ammo_left -= 1
    bullet.pendown()
    bullet.setpos(x, y)
    bullet.showturtle()
    bullet.clear()
    
    for e in enemies:
      
      if distFrom(e, bullet) <= 25:
        kills += 1
        print("YOU GOT ONE! -- Bullets left:", ammo_left, "-- Sleeps:", kills)
        bullet.hideturtle()
        e.hideturtle()
        e.setpos(rnum(-450, 450), rnum(-200, 200))
        e.showturtle()
        break
    
    if bullet.isvisible():
      print("YOU MISSED! -- Bullets left:", ammo_left)
      bullet.hideturtle()
      
    player_can_shoot = True   # UNLOCK SHOOTING
  
  elif not player_can_shoot: print("Still shooting...")
  else: print("NO AMMO!!!!!!!")

screen.onclick(shoot)
```

If I taught you well, then this code snippet should make you shudder. Multiple global variables being haphazardly modified on the fly from a single function? Various entities being moved and changed all in a giant jumbled mess? Hard-coded values for collisions? Print statements? All these things should ellicit either a shriek of fright or a fainting episode.

There's no doubt about it: *this is bad code*. But why? And how is what we did better? And even if it is, how does that excuse spending so much time writing classes when all of this could have been achieved much more quickly and easily by simply writing top-level functions on a limited number of turtle entities?

<h3>Why this code is bad</h3>

**1. It is incredibly difficult to make changes to object behaviors.**

  Suppose I want to change it so the bullet can pierce infinite enemies (our game does this by default). First of all, I'd have to figure out where that behavior is written in, because it's not at all obvious. Eventually, I realize it's embedded in the part that loops over the enemies. Ok, so how do we change it? Well, it's the `break` statement that stops us after we hit an enemy, so what if we just remove that? Well, sure, that will work. But then our bullet will turn invisible after the first enemy even though it will keep going and hitting more enemies. And what if we want to have multiple bullets on screen at the same time (like in our game, where you can shoot as fast as you can click)? Well, you'd have to rewrite almost the entire thing, scraping out every piece of logic that relies on the `player_can_shoot` Boolean and somehow working in a system by which the game can render arbitrarily many bullets at once.
  
  This is a mess. Because so many different entities and behaviors are lumped into one, and because all of it is wrapped in one giant, vague `shoot()` function, it is a monumental task to make even simple gameplay modifications. And, if you're actually trying to design a fun game, modifications and testing out new features to see what feels good is a critical part of the design process.
  
**2. It is painful to read.**

This kind of goes hand in hand with what I said above, but to someone with fresh eyes, this code is mysterious and confusing. Because the animation of each entity, ammo logic, scoring system, player feedback, and user input are all lumped into one big chunk of code, it's almost impossible to tell what does what and why. Sure, you could add a bajillion comments, but taking the extra effort to write cleanly organized code will make it easier for someone new (or you in 3 weeks) to look at this and understand more quickly what's going on.

**3. It is prone to bugs.**

This is a relatively simple function, but it is easy to see that structuring functions like this at a larger scale will result in intensely complicated things happening in a very obtuse manner. That is an ominous precondition for software bugs. With so much going on at once, it would incredibly easy for me to forget to include some small but important feature that bites me in the butt later down the line. Without clear, distinguished inputs and outputs for every individual operation going on here, it's practically guaranteed that I'm going to forget something or create some unexpected interaction between variables that I won't realize until much later.

It's not just a problem in terms of *creating* bugs, but also *fixing* them. If I forget to hide my enemy turtle before I reset it to another place on the screen, I'll get an animation bug and, since it's a logic error with no helpful traceback, I'll have to track it down to the most unlikely place: the collision resolution. Debugging code like this is a nightmare.

<h3>How to do better</h3>

Read. Seriously. Read programming books. I don't mean tutorials, I mean *books*. Thick ones, with lots of jargon, written by people with Ph.D.s for people who want to understand not just how to write code, but how to write code that can be modified, maintained, and proudly shared with the world. Code that is not just functional but beautiful, inspiring, and feels good to write. I'm getting too poetic. Here's the thing: everyone will tell you the best way to get good at coding is to code. And that's true. But the best way to get AMAZING at coding is to read and *then* code.

A good book to look at (that I used as a reference during this class) is Robert Nystrom's [Game Programming Patterns](https://gameprogrammingpatterns.com/). If you want a more eloquent explanation of what I'm talking about with reference to software design and good coding habits, read his short [introduction](https://gameprogrammingpatterns.com/architecture-performance-and-games.html).

For just starting out, don't worry too much. Focus on exploring, trying things out on your own, writing your own programs. Get stuck, look up tutorials to pull yourself out of the hole you're in. That's fine. I encourage that. But when you feel confident enough to want to do something bigger, hold back and realize that while you've learned everything about software and actually writing code to get stuff done, you've learned almost nothing about *design*.

Anyone can write code that does pretty much what you want. Lots of people do that and do it fast, or use tricks you have never even heard of. But to write that beautiful, inspiring, joyful code I was talking about? That's about design, and that's, like, 80% of what makes good code.

Unfortunately, I can't teach you design. For one thing, I'm still pretty terrible at it. I have a lot to learn and I wouldn't trust myself to impart ill-gotten lessons on impressionable beginning programmers.

Books can't teach you design either. You have to figure that out yourself, through the practice I was mentioning. But how do you know what to practice? That's where the books come in. They can't teach you design, but they can teach you design *patterns*.

**I'd be hard-pressed to accurately define what I mean, so let's finish this off by going over an example.** Remember when, after writing a working game, I seemingly for no reason tore apart our entire existing codebase and shoved it all into different classes, each entity kicking and screaming as I locked it into its own lonely .py file? That was all in service of this holy thing I kept gushing on about called "gamestate," which is a very simplified version of a real-world design pattern. I didn't write it to fix a bug. I wrote it to ensure that everything we wrote *after that* would be better organized, easier to debug, easier to maintain and improve. It was a solution to a problem that did not exist yet. That, in a nutshell, is design. The *process*, I mean. The part where we put our heads together to figure out what should go where and what class should be responsible for what behavior, and how they should interact. All that brainpower we spent fixing problems before they even happened. That comes with practice.

But to get yourself started, you can learn some of the types of designs that come in handy, called design patterns. These aren't pieces of code you can copy from a tutorial, nor are they a checklist of things to do. They are a way of thinking about a problem, particularly the problems that arise when deciding how to structure and optimize your code. In writing games, one of the problems that comes up a lot is how various entities should communicate with each other (e.g. the player and the scoreboard or the bullet and the enemy). One of the (many) associated design patterns that can give you a starting point for how to think about and approach this problem is the *mediator*. This is the *idea* of the thing (not the thing itself) that managed interactions between entities by holding some global data which each separate *component* can access. In our example, the mediator was the `Game` class, and the data was held in a dictionary called `gamestate`. I applied a crude version of an established pattern to solve a design problem.

You might notice that (unless I made a mistake somewhere), nowhere does any component entity (such as `Food`, `Player`, or `Bullet`) actually modify the `gamestate` directly. Instead, the `Game` extracts data from each of these subclasses in order to keep track of what's going on, and then hands the updated data to someone else. It does this about 30 times a second, if running smoothly. This was a design decision, based on a pattern I knew. But I was not copying code or fulfilling a set of instructions; in fact, it's possible to achieve the same result by doing it in a very different way. For instance: many implementations of mediators actually rely on component entities to update the global data themselves. In our example, that would be like the `Player` class directly accessing `gamestate["score"]` and updating it, instead of `Game` reaching into `Player.score` to update `gamestate["score"]` during `update_gamestate()`. Some implementations that solve the problem at hand don't use a mediator at all; a simple alternative is having each component access each other directly, which would be possible if we passed a direct link to `Game.enemies` (the list containing each instance of the `Enemy` class) to `Bullet.update()` every frame and had `Bullet` directly call something like `Enemy.destroy()` if they collide. A more complicated solution would be to forgo a mediator and instead have some sort of global messaging system by which each component could tell every other component what it is up to, but without directly commanding other entities to do stuff. So in this case, `Bullet` would simply announce to every `Enemy` that it had a collision with enemy #17, for example, and then enemy #17 would receive this message and know to destroy itself.

The fact that I chose to use a simple mediator was a design decision, and it had advantages and tradeoffs. For one thing, it required an extra class, `Game`, which we probably could have avoided if we used a broadcasting system or direct contact. But it definitely uses less code in each component class, so that's an advantage, and it's more apparently clear what is happening at all times because with zero exceptions, all externalized behavior can be found somewhere in `Game.update()`. That kind of centralization was a boon to our programming experience and it made debugging extremely easy. I never spent more than 20 minutes tracking a bug down, and adding features had a kind of familiar rhythm to it: add some instance variables and methods to a particular component class, then add in a call to that method in the appropriate place in `Game.update()`. If the change affected two classes, their changes would be completely disjoint (meaning no overlap) because where one's change might *add* data to the `gamestate`, the other might then take the `gamestate` as input to respond to it. Thus, their interactive behavior was *mediated* by `Game`.

By knowing and applying this pattern in the way that best suited our particular problem, I was doing design. The point of spending so much time talking about it was to impress upon you the importance of such practices and teach you some tricks to keep in mind when you write your own programs.

<h3>Conclusion</h3>

If you actually stuck through and read this, first of all, thank you. I hope this gives you some sense of why we did the things that we did rather than just focusing on making a fun game. If I did my job well, then now you have a firm basis on which to go out and make your own stuff, which should hopefully be more interesting than our silly turtle game, but you'll take with you the more general lessons about careful planning and organization and structure, and you'll never write code like that monstrosity I showed you earlier. That's all for now.

Organization is king.
List comprehensions are awesome.
Remember the &#955;.

-- Gregory
