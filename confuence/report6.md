## Smolvla 1.1

| Sno | Actions                                        | Pass/Fail |
|-----|------------------------------------------------|-----------|
|  1  | Rest                                           | Fail      |
|  2  | Right hand to right side movement closed/open  | Pass      |
|  3  | Right hand to Top closed                       | Pass      |
|  4  | Left hand to left side closed                  | Pass      |
|  5  | Left hand to left side open                    | Pass      |
|  6  | Right hand to Home Position closed/open        | Pass      |
|  7  | Left hand to Top closed                        | Fail      |
|  8  | Left hand to home closed/open                  | Pass      |

**Observation:** Stability and smoothness is moderate. Gripper failure is seen often.

---

## Smolvla v2

| Sno | Actions                                        | Pass/Fail |
|-----|------------------------------------------------|-----------|
|  1  | Rest                                           | Pass      |
|  2  | Right hand to right side movement closed/open  | Pass      |
|  3  | Right hand to Top closed                       | Pass      |
|  4  | Left hand to left side closed                  | Pass      |
|  5  | Left hand to left side open                    | Pass      |
|  6  | Right hand to Home Position closed/open        | Pass      |
|  7  | Left hand to Top closed                        | Fail      |
|  8  | Left hand to home closed/open                  | Pass      |

**Observation:** Stable and smooth. Gripper failure seen only in left hand.

---

## Smolvla v3

| Sno | Actions                                        | Pass/Fail |
|-----|------------------------------------------------|-----------|
|  1  | Rest                                           | Fail      |
|  2  | Right hand to right side movement closed/open  | Pass      |
|  3  | Right hand to Top closed                       | Pass      |
|  4  | Left hand to left side closed                  | Pass      |
|  5  | Left hand to left side open                    | Pass      |
|  6  | Right hand to Home Position closed/open        | Pass      |
|  7  | Left hand to Top closed                        | Fail      |
|  8  | Left hand to home closed/open                  | Pass      |

**Observation:** Stability and smoothness is poor. Gripper failure seen.

---

## Overall Details

| Release Version | Eager: Inference (FPS) | Eager: Control Loop (FPS) | Performant: Inference (FPS) | Performant: Control Loop (FPS) |
|-----------------|------------------------|---------------------------|-----------------------------|--------------------------------|
| SmolVLA V1.1    | 15.95                  | 27.332                    | 17.98                       | 24.400                         |
| SmolVLA V2.0    | 17.88                  | 27.094                    | 21.53                       | 22.076                         |
| SmolVLA V3.0    | 18.54                  | 26.771                    | 20.42                       | 23.520                         |

> **Note:** Data collected using Eager Mode.

---

**Next Action:** Enable compile cache on LeRobot and improve control loop.

**Recommendation:** SmolVLA V2 with eager mode is preferred.
