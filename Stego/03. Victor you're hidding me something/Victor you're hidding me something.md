# **Victor you're hidding me something**

```
Fort heureux l'homme qui trouvera
La vérité au travère des noires
Abysses d'une âme tourmenter par la
Galère d'un amour improbable.

Ces âmes que tu rappelles,
Mon coeur, ne reviennent pas.
Pourquoi donc s'obstinent-elles,
Hélas ! à rester là-bas ?

Dans les sphères éclatantes,
Dans l'azur et les rayons,
Sont-elles donc plus contentes
Qu'avec nous qui les aimions ?

Nous avions sous les tonnelles
Une maison près Saint-Leu.
Comme les fleurs étaient belles !
Comme le ciel était bleu !

Parmi les feuilles tombées,
Nous courions au bois vermeil ;
Nous cherchions des scarabées
Sur les vieux murs au soleil ;

On riait de ce bon rire
Qu'Éden jadis entendit,
Ayant toujours à se dire
Ce qu'on s'était déjà dit ;

Je contais la Mère l'Oie ;
On était heureux, Dieu sait !
On poussait des cris de joie
Pour un oiseau qui passait.
```

Just concatenate the first letters of each line.

Here has no reliable clue, except the first letter of first paragraph is "FLAG".

Just take a try, cuz i can't find the orginal reference of this poem(?).

Save the text as a text file.
```shell=
$ grep -Po '^.' test.txt | tr -d '\n'
FLAGCMPHDDSQNUCCPNNSOQACJOOP
```


