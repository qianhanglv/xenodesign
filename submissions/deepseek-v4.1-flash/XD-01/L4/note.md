# X-DONUT-001 · L4 · motion.svg

Source: L0 X-DONUT-001 (creature.svg).
One self-contained animated SVG (SMIL, no script, no external file), 512 × 512,
loop 3.2 s, seamless: the last keyframe is the first one.

MOTION: 3.2 s loop. Phase map, as fractions of the loop: 0.00-0.15 idle (a slow
breath, 3 cm of shell rise and fall); 0.15-0.60 run, two short hops; 0.60-0.92
the jump, with a deep crouch at 0.74, the push at 0.79, the apex at 0.84 and the
drop at 0.89; 0.92-0.97 the landing, one heavy compression at 0.93; then the
settle back into the first idle pose at 1.00. Twenty keyframes drive the cycle.

CONTACT: the feet are planted on the ground plane from 0.00 to 0.23 in the crouch
and the push, again on every landing (0.41, 0.62, 0.93) and through the settle;
they leave the ground only inside the two hops and the jump. The body drops over
planted feet and the knees take the load, so weight is read at the knees, not at
the shell. During flight the legs stay under the shell and do not splay.

FRAMES: 20 SMIL keyframes, each a full pose (body offset plus eight joint angles,
solved by two-bone IK so the foot lands where the ground is, not where a rotation
happens to put it). No limb is drawn twice and no intermediate tween invents a
fifth limb.

Q1 -> the shell is one rigid group for the whole cycle. The bore cannot collapse,
telegraph, or change area, because nothing inside the shell group is animated:
the group only translates with the body. Measured at every keyframe: the mouth
keeps 0.39 of the shell silhouette and never moves relative to the shell.

P1 -> the same 2.1 m shell in every frame.
P2 -> the same flat stone facets in every frame; no part becomes soft in motion.
F1 -> the ember light under the shell is constant; the shadow side stays warm.
F2/F4 -> the maws and the vibration plate travel with the shell, unchanged; the
right manipulator is the striker and swings during the idle, at the same beat as
the breath.
F3 -> the crystal blades ride with the shell and never detach.
Q2/Q3/Q4 -> 4 limbs in every keyframe; 2 legs and 2 manipulators; the legs are
the two IK chains reaching the ground, the manipulators are the two upper chains
that never touch the ground.
Q5 -> no eyes in any frame; the front face stays bare.
Q6 -> three maws in every frame, same row, same sizes.
N1 -> the shell does not bend: no spine is implied by the animation, since the
only deforming parts are the four limb chains.

RECONCILE -> T-01: the two leg chains carry the ground contact, the two
manipulator chains swing free. 2 + 2 = 4 at every keyframe.

Not animated on purpose: the mouth, the maw rims, the crest, the vibration
plate. A rigid shell is the point of the animal; only the limbs and the body
height move.
