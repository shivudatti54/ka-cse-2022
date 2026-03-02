# Case Study: SMS Telephony and Location Based Services

=============================================

## Introduction

---

- SMS (Short Message Service) is a standard for delivering short text messages between mobile devices.
- Location-based services (LBS) use GPS and other technologies to provide location information to users.

## SMS Telephony

---

- **SMS Architecture**:
  - 2G/3G networks
  - SMS Gateways
  - Mobile Devices
  - SMS Centers
- **SMS Protocols**:
  - GSM/CDMA protocols
  - SMPP (Short Message Peer-to-Peer)
  - SS7 (Signaling System 7)
- **SMS Characteristics**:
  - Limited character count (160 characters)
  - No multimedia support

## Location Based Services

---

- **LBS Architecture**:
  - GPS receivers
  - Location servers
  - Mobile devices
  - LBS applications
- **LBS Protocols**:
  - GPS protocol
  - OTGS (Object Transfer Protocol for GPS)
  - WGS-84 (World Geodetic System 1984)
- **LBS Characteristics**:
  - Location accuracy (up to 100m)
  - Location update frequency (every few seconds)

## Comparison

---

- **SMS vs LBS**:
  - SMS is limited to text messages, while LBS provides location information.
  - SMS is typically used for simple messages, while LBS is used for more complex applications.

## Formula/Definition/Theorem

---

- **GPS formula**:
  - `lat = arctan(2 \* tan(lat/2) \* sin(Δlat / 2))`
  - `lon = arctan(2 \* tan(lon/2) \* sin(Δlon / 2))`
- **SMS protocol formula**:
  - `SMPP protocol: SMPP = (SMSC, SMGR, MSISDN, SMSCID)`
- **LBS theorem**:
  - "The law of cosines states that for any triangle with sides of length a, b, and c, and angle C opposite side c, c² = a² + b² - 2ab \* cos(C)".
