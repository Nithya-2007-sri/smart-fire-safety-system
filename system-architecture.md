# System Architecture

## 1. Overview

The proposed Smart Fire-Safety System uses multiple sensing, monitoring, verification, and emergency-response stages to support fire safety in firecracker manufacturing units.

## 2. System Workflow

**Prevention → Detection → Verification → Isolation → Evacuation → Suppression Assessment**

## 3. Functional Blocks

### 3.1 Ignition Prevention

ESD mats, grounding checks, and appropriate handling procedures are proposed to help reduce electrostatic ignition risks.

### 3.2 Sensor Layer

The proposed sensing layer includes:

- Flame detection
- Smoke detection
- Temperature monitoring

Sensor selection and placement must be determined through professional risk assessment and testing.

### 3.3 Monitoring and Verification

A microcontroller-based monitoring unit receives sensor signals and evaluates abnormal conditions. The verification logic must be tested to reduce false alarms and missed detections.

### 3.4 Emergency Response

When a fire event is confirmed, the proposed system may:

- Activate audible and visual alarms
- Initiate suitable emergency electrical isolation
- Send Tamil voice evacuation instructions
- Activate LED-guided evacuation indicators
- Trigger an appropriately designed emergency door-release mechanism

Life-safety functions must be designed so that a controller or power failure does not prevent safe evacuation.

### 3.5 Suppression Assessment

A suitable suppression method may be evaluated as an additional safety layer. Nitrogen-based suppression is only a concept at this stage and requires specialist engineering, oxygen-deficiency assessment, controlled testing, and regulatory approval.

## 4. Architecture Flow

```text
ESD Prevention and Grounding
             |
             v
   Flame / Smoke / Temperature
             |
             v
     Monitoring Controller
             |
             v
     Event Verification
             |
             v
      Emergency Response
             |
      +------+------+
      |      |      |
      v      v      v
    Alarm  Isolation Evacuation
                       |
                       v
              Guided Exit Support
```

## 5. Design Considerations

- Sensor reliability and placement
- False-alarm and missed-detection testing
- Backup power and fault handling
- Safe electrical isolation
- Accessible evacuation routes
- Independent and fail-safe life-safety controls
- Compliance with applicable industrial safety standards

## 6. Current Status

This document describes a proposed functional architecture. The system has not been claimed as implemented or experimentally validated unless supporting evidence is added.
