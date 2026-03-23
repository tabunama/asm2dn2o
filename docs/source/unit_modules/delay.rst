delay
=====

Purpose
-------

``delay`` provides a hydraulic delay / first-order lag block for 56-state process
streams. It is especially useful for recycle-loop closure and simple transport
representation in explicit plant-wide simulations.

Public usage pattern
--------------------

The practical public wrapper is often presented as something like:

- ``DelayBlock(XINIT_DELAY, T_DELAY)``
- then ``step(u56, dt)``

The low-level C implementation is built around two functions:

- ``delay_asm2d_init(...)``
- ``delay_asm2d_step(...)``

Initialization
--------------

The initialization function directly copies the provided initial vector into the
internal delay state. The current wrapper convention is to provide a delay
initialization vector consistent with the transported stream.

Time constant and solver behavior
---------------------------------

The delay step function uses:

- an incoming stream ``u``,
- a time constant ``T``,
- an explicit step size ``dt``.

Internally, it applies a first-order lag with explicit Euler integration.

Input sanitization
------------------

The C core includes robust input cleaning before the update:

- invalid numbers such as NaN or Inf are replaced,
- negative concentrations are clipped to zero,
- flow is protected with a minimum value to avoid division by near-zero.

This is important because the delay block is often the first place where noisy
measured data, recycle closure, or interpolation artifacts show up.

How the state is represented
----------------------------

The delay does not lag concentrations directly for every state. Instead, for most
states it works on a mass-like representation:

- target mass = concentration * flow

Special handling is applied to:

- flow,
- temperature.

That design makes the block more robust when flow varies over time.

No-delay limit
--------------

If the time constant is effectively zero, the implementation switches to a no-delay
behavior:

- flow follows the incoming flow directly,
- temperature follows directly,
- other states are forced to the instantaneous mass targets.

This gives a stable bypass-like behavior instead of an unstable stiff update.

Output reconstruction
---------------------

After updating the internal state, the delay block reconstructs the output stream:

- concentration-like states are divided by safe output flow,
- flow is passed as the delayed flow state,
- temperature is passed as the delayed temperature state.

This means the delay output remains compatible with the standard 56-state stream
interface used by the other units.

Typical use cases
-----------------

- hydraulic transport between mixing and reactor blocks,
- recycle-loop causal closure,
- simple representation of travel time in measured-data replay,
- smoothing of abrupt upstream stream changes.

Recommended wrapper features
----------------------------

In project-level Python wrappers, two extra features are often useful:

- internal substepping when the external ``dt`` is large relative to ``T_DELAY``,
- explicit conversion between concentration-style initialization and the internal
  mass-style state representation.

These features belong naturally in the user wrapper, while the compiled core keeps
the fundamental lag behavior compact and predictable.

Important caveats
-----------------

- The current implementation is an explicit first-order lag, not a full distributed
  transport model.
- Very large ``dt`` values relative to ``T`` may still justify substepping in the
  wrapper.
- Users should verify that the delay initialization is consistent with the intended
  transported stream.
