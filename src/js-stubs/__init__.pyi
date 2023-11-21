# @formatter:off

from typing import overload, Any, Awaitable, Sequence, Literal, TypedDict, NotRequired
USVString = str


SecurityPolicyViolationEventDisposition = Literal["enforce", "report"]

EndingType = Literal["transparent", "native"]

IDBRequestReadyState = Literal["pending", "done"]

IDBTransactionDurability = Literal["default", "strict", "relaxed"]

IDBCursorDirection = Literal["next", "nextunique", "prev", "prevunique"]

IDBTransactionMode = Literal["readonly", "readwrite", "versionchange"]

KeyType = Literal["public", "private", "secret"]

KeyUsage = Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]

KeyFormat = Literal["raw", "spki", "pkcs8", "jwk"]

AccelerometerLocalCoordinateSystem = Literal["device", "screen"]

AutoplayPolicy = Literal["allowed", "allowed-muted", "disallowed"]

AutoplayPolicyMediaType = Literal["mediaelement", "audiocontext"]

BackgroundFetchResult = Literal["", "success", "failure"]

BackgroundFetchFailureReason = Literal["", "aborted", "bad-status", "fetch-error", "quota-exceeded", "download-total-exceeded"]

PresentationStyle = Literal["unspecified", "inline", "attachment"]

PressureState = Literal["nominal", "fair", "serious", "critical"]

PressureFactor = Literal["thermal", "power-supply"]

PressureSource = Literal["cpu"]

ContactProperty = Literal["address", "email", "icon", "name", "tel"]

ContentCategory = Literal["", "homepage", "article", "video", "audio"]

CookieSameSite = Literal["strict", "lax", "none"]

CredentialMediationRequirement = Literal["silent", "optional", "conditional", "required"]

ScriptingPolicyViolationType = Literal["externalScript", "inlineScript", "inlineEventHandler", "eval"]

FontFaceLoadStatus = Literal["unloaded", "loading", "loaded", "error"]

FontFaceSetLoadStatus = Literal["loading", "loaded"]

HighlightType = Literal["highlight", "spelling-error", "grammar-error"]

ChildDisplayType = Literal["block", "normal"]

LayoutSizingMode = Literal["block-like", "manual"]

BlockFragmentationType = Literal["none", "page", "column", "region"]

BreakType = Literal["none", "line", "column", "page", "region"]

SpatialNavigationDirection = Literal["up", "down", "left", "right"]

FocusableAreaSearchMode = Literal["visible", "all"]

CSSNumericBaseType = Literal["length", "angle", "time", "frequency", "resolution", "flex", "percent"]

CSSMathOperator = Literal["sum", "product", "negate", "invert", "min", "max", "clamp"]

ScrollBehavior = Literal["auto", "smooth"]

ScrollLogicalPosition = Literal["start", "center", "end", "nearest"]

CSSBoxType = Literal["margin", "border", "padding", "content"]

DevicePostureType = Literal["continuous", "folded", "folded-over"]

ItemType = Literal["product", "subscription"]

ShadowRootMode = Literal["open", "closed"]

SlotAssignmentMode = Literal["manual", "named"]

MediaKeysRequirement = Literal["required", "optional", "not-allowed"]

MediaKeySessionType = Literal["temporary", "persistent-license"]

MediaKeySessionClosedReason = Literal["internal-error", "closed-by-application", "release-acknowledged", "hardware-context-reset", "resource-evicted"]

MediaKeyStatus = Literal["usable", "expired", "released", "output-restricted", "output-downscaled", "usable-in-future", "status-pending", "internal-error"]

MediaKeyMessageType = Literal["license-request", "license-renewal", "license-release", "individualization-request"]

RequestDestination = Literal["", "audio", "audioworklet", "document", "embed", "font", "frame", "iframe", "image", "manifest", "object", "paintworklet", "report", "script", "sharedworker", "style", "track", "video", "worker", "xslt"]

RequestMode = Literal["navigate", "same-origin", "no-cors", "cors"]

RequestCredentials = Literal["omit", "same-origin", "include"]

RequestCache = Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]

RequestRedirect = Literal["follow", "error", "manual"]

RequestDuplex = Literal["half"]

RequestPriority = Literal["high", "low", "auto"]

ResponseType = Literal["basic", "cors", "default", "error", "opaque", "opaqueredirect"]

FileSystemPermissionMode = Literal["read", "readwrite"]

WellKnownDirectory = Literal["desktop", "documents", "downloads", "music", "pictures", "videos"]

FileSystemHandleKind = Literal["file", "directory"]

WriteCommandType = Literal["write", "seek", "truncate"]

FullscreenNavigationUI = Literal["auto", "show", "hide"]

GamepadHand = Literal["", "left", "right"]

GamepadHapticsResult = Literal["complete", "preempted"]

GamepadHapticActuatorType = Literal["vibration", "dual-rumble"]

GamepadHapticEffectType = Literal["dual-rumble"]

GamepadMappingType = Literal["", "standard", "xr-standard"]

MockSensorType = Literal["ambient-light", "accelerometer", "linear-acceleration", "gravity", "gyroscope", "magnetometer", "uncalibrated-magnetometer", "absolute-orientation", "relative-orientation", "geolocation", "proximity"]

GyroscopeLocalCoordinateSystem = Literal["device", "screen"]

DocumentReadyState = Literal["loading", "interactive", "complete"]

DocumentVisibilityState = Literal["visible", "hidden"]

CanPlayTypeResult = Literal["", "maybe", "probably"]

TextTrackMode = Literal["disabled", "hidden", "showing"]

TextTrackKind = Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]

SelectionMode = Literal["select", "start", "end", "preserve"]

PredefinedColorSpace = Literal["srgb", "display-p3"]

CanvasFillRule = Literal["nonzero", "evenodd"]

ImageSmoothingQuality = Literal["low", "medium", "high"]

CanvasLineCap = Literal["butt", "round", "square"]

CanvasLineJoin = Literal["round", "bevel", "miter"]

CanvasTextAlign = Literal["start", "end", "left", "right", "center"]

CanvasTextBaseline = Literal["top", "hanging", "middle", "alphabetic", "ideographic", "bottom"]

CanvasDirection = Literal["ltr", "rtl", "inherit"]

CanvasFontKerning = Literal["auto", "normal", "none"]

CanvasFontStretch = Literal["ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "normal", "semi-expanded", "expanded", "extra-expanded", "ultra-expanded"]

CanvasFontVariantCaps = Literal["normal", "small-caps", "all-small-caps", "petite-caps", "all-petite-caps", "unicase", "titling-caps"]

CanvasTextRendering = Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"]

OffscreenRenderingContextId = Literal["2d", "bitmaprenderer", "webgl", "webgl2", "webgpu"]

ScrollRestoration = Literal["auto", "manual"]

DOMParserSupportedType = Literal["text/html", "text/xml", "application/xml", "application/xhtml+xml", "image/svg+xml"]

ImageOrientation = Literal["from-image", "flipY"]

PremultiplyAlpha = Literal["none", "premultiply", "default"]

ColorSpaceConversion = Literal["none", "default"]

ResizeQuality = Literal["pixelated", "low", "medium", "high"]

WorkerType = Literal["classic", "module"]

UserIdleState = Literal["active", "idle"]

ScreenIdleState = Literal["locked", "unlocked"]

RedEyeReduction = Literal["never", "always", "controllable"]

FillLightMode = Literal["auto", "off", "flash"]

MeteringMode = Literal["none", "manual", "single-shot", "continuous"]

JsonLdErrorCode = Literal["colliding keywords", "conflicting indexes", "context overflow", "cyclic IRI mapping", "invalid @id value", "invalid @import value", "invalid @included value", "invalid @index value", "invalid @nest value", "invalid @prefix value", "invalid @propagate value", "invalid @protected value", "invalid @reverse value", "invalid @version value", "invalid base direction", "invalid base IRI", "invalid container mapping", "invalid context entry", "invalid context nullification", "invalid default language", "invalid IRI mapping", "invalid JSON literal", "invalid keyword alias", "invalid language map value", "invalid language mapping", "invalid language-tagged string", "invalid language-tagged value", "invalid local context", "invalid remote context", "invalid reverse property map", "invalid reverse property value", "invalid reverse property", "invalid scoped context", "invalid script element", "invalid set or list object", "invalid term definition", "invalid type mapping", "invalid type value", "invalid typed value", "invalid value object value", "invalid value object", "invalid vocab mapping", "IRI confused with prefix", "keyword redefinition", "loading document failed", "loading remote context failed", "multiple context link headers", "processing mode conflict", "protected term redefinition"]

JsonLdFramingErrorCode = Literal["invalid frame", "invalid @embed value"]

JsonLdEmbed = Literal["@always", "@once", "@never"]

MagnetometerLocalCoordinateSystem = Literal["device", "screen"]

AppBannerPromptOutcome = Literal["accepted", "dismissed"]

MediaDecodingType = Literal["file", "media-source", "webrtc"]

MediaEncodingType = Literal["record", "webrtc"]

HdrMetadataType = Literal["smpteSt2086", "smpteSt2094-10", "smpteSt2094-40"]

ColorGamut = Literal["srgb", "p3", "rec2020"]

TransferFunction = Literal["srgb", "pq", "hlg"]

ReadyState = Literal["closed", "open", "ended"]

EndOfStreamError = Literal["network", "decode"]

AppendMode = Literal["segments", "sequence"]

MockCapturePromptResult = Literal["granted", "denied"]

CaptureAction = Literal["next", "previous", "first", "last"]

MediaStreamTrackState = Literal["live", "ended"]

VideoFacingModeEnum = Literal["user", "environment", "left", "right"]

VideoResizeModeEnum = Literal["none", "crop-and-scale"]

MediaDeviceKind = Literal["audioinput", "audiooutput", "videoinput"]

MediaSessionPlaybackState = Literal["none", "paused", "playing"]

MediaSessionAction = Literal["play", "pause", "seekbackward", "seekforward", "previoustrack", "nexttrack", "skipad", "stop", "seekto", "togglemicrophone", "togglecamera", "hangup", "previousslide", "nextslide"]

BitrateMode = Literal["constant", "variable"]

RecordingState = Literal["inactive", "recording", "paused"]

RTCDegradationPreference = Literal["maintain-framerate", "maintain-resolution", "balanced"]

NavigationHistoryBehavior = Literal["auto", "push", "replace"]

NavigationFocusReset = Literal["after-transition", "manual"]

NavigationScrollBehavior = Literal["after-transition", "manual"]

NavigationType = Literal["reload", "push", "replace", "traverse"]

NavigationTimingType = Literal["navigate", "reload", "back_forward", "prerender"]

ConnectionType = Literal["bluetooth", "cellular", "ethernet", "mixed", "none", "other", "unknown", "wifi", "wimax"]

EffectiveConnectionType = Literal["2g", "3g", "4g", "slow-2g"]

NotificationPermission = Literal["default", "denied", "granted"]

NotificationDirection = Literal["auto", "ltr", "rtl"]

OrientationSensorLocalCoordinateSystem = Literal["device", "screen"]

ClientLifecycleState = Literal["active", "frozen"]

PaymentDelegation = Literal["shippingAddress", "payerName", "payerPhone", "payerEmail"]

PaymentShippingType = Literal["shipping", "delivery", "pickup"]

PaymentComplete = Literal["fail", "success", "unknown"]

PermissionState = Literal["granted", "denied", "prompt"]

PresentationConnectionState = Literal["connecting", "connected", "closed", "terminated"]

PresentationConnectionCloseReason = Literal["error", "closed", "wentaway"]

PushEncryptionKeyName = Literal["p256dh", "auth"]

ReferrerPolicy = Literal["", "no-referrer", "no-referrer-when-downgrade", "same-origin", "origin", "strict-origin", "origin-when-cross-origin", "strict-origin-when-cross-origin", "unsafe-url"]

RemotePlaybackState = Literal["connecting", "connected", "disconnected"]

ResizeObserverBoxOptions = Literal["border-box", "content-box", "device-pixel-content-box"]

RenderBlockingStatusType = Literal["blocking", "non-blocking"]

TaskPriority = Literal["user-blocking", "user-visible", "background"]

CaptureStartFocusBehavior = Literal["focus-captured-surface", "no-focus-change"]

SelfCapturePreferenceEnum = Literal["include", "exclude"]

SystemAudioPreferenceEnum = Literal["include", "exclude"]

SurfaceSwitchingPreferenceEnum = Literal["include", "exclude"]

DisplayCaptureSurfaceType = Literal["monitor", "window", "browser"]

CursorCaptureConstraint = Literal["never", "always", "motion"]

OrientationLockType = Literal["any", "natural", "landscape", "portrait", "portrait-primary", "portrait-secondary", "landscape-primary", "landscape-secondary"]

OrientationType = Literal["portrait-primary", "portrait-secondary", "landscape-primary", "landscape-secondary"]

WakeLockType = Literal["screen"]

ScrollAxis = Literal["block", "inline", "horizontal", "vertical"]

TransactionAutomationMode = Literal["none", "autoAccept", "autoReject", "autoOptOut"]

ParityType = Literal["none", "even", "odd"]

FlowControlType = Literal["none", "hardware"]

ServiceWorkerState = Literal["parsed", "installing", "installed", "activating", "activated", "redundant"]

ServiceWorkerUpdateViaCache = Literal["imports", "all", "none"]

FrameType = Literal["auxiliary", "top-level", "nested", "none"]

ClientType = Literal["window", "worker", "sharedworker", "all"]

LandmarkType = Literal["mouth", "eye", "nose"]

BarcodeFormat = Literal["aztec", "code_128", "code_39", "code_93", "codabar", "data_matrix", "ean_13", "ean_8", "itf", "pdf417", "qr_code", "unknown", "upc_a", "upc_e"]

SpeechRecognitionErrorCode = Literal["no-speech", "aborted", "audio-capture", "network", "not-allowed", "service-not-allowed", "bad-grammar", "language-not-supported"]

SpeechSynthesisErrorCode = Literal["canceled", "interrupted", "audio-busy", "audio-hardware", "network", "synthesis-unavailable", "synthesis-failed", "language-unavailable", "voice-unavailable", "text-too-long", "invalid-argument", "not-allowed"]

ReadableStreamReaderMode = Literal["byob"]

ReadableStreamType = Literal["bytes"]

TouchType = Literal["direct", "stylus"]

ImportExportKind = Literal["function", "table", "memory", "global"]

TableKind = Literal["externref", "anyfunc"]

ValueType = Literal["i32", "i64", "f32", "f64", "v128", "externref", "anyfunc"]

IterationCompositeOperation = Literal["replace", "accumulate"]

AnimationPlayState = Literal["idle", "running", "paused", "finished"]

AnimationReplaceState = Literal["active", "removed", "persisted"]

FillMode = Literal["none", "forwards", "backwards", "both", "auto"]

PlaybackDirection = Literal["normal", "reverse", "alternate", "alternate-reverse"]

CompositeOperation = Literal["replace", "add", "accumulate"]

CompositeOperationOrAuto = Literal["replace", "add", "accumulate", "auto"]

LockMode = Literal["shared", "exclusive"]

OTPCredentialTransportType = Literal["sms"]

AudioContextState = Literal["suspended", "running", "closed"]

AudioContextLatencyCategory = Literal["balanced", "interactive", "playback"]

AudioSinkType = Literal["none"]

ChannelCountMode = Literal["max", "clamped-max", "explicit"]

ChannelInterpretation = Literal["speakers", "discrete"]

AutomationRate = Literal["a-rate", "k-rate"]

BiquadFilterType = Literal["lowpass", "highpass", "bandpass", "lowshelf", "highshelf", "peaking", "notch", "allpass"]

OscillatorType = Literal["sine", "square", "sawtooth", "triangle", "custom"]

PanningModelType = Literal["equalpower", "HRTF"]

DistanceModelType = Literal["linear", "inverse", "exponential"]

OverSampleType = Literal["none", "2x", "4x"]

AuthenticatorAttachment = Literal["platform", "cross-platform"]

ResidentKeyRequirement = Literal["discouraged", "preferred", "required"]

AttestationConveyancePreference = Literal["none", "indirect", "direct", "enterprise"]

TokenBindingStatus = Literal["present", "supported"]

PublicKeyCredentialType = Literal["public-key"]

AuthenticatorTransport = Literal["usb", "nfc", "ble", "hybrid", "internal"]

UserVerificationRequirement = Literal["required", "preferred", "discouraged"]

LargeBlobSupport = Literal["required", "preferred"]

AacBitstreamFormat = Literal["aac", "adts"]

AvcBitstreamFormat = Literal["annexb", "avc"]

HevcBitstreamFormat = Literal["annexb", "hevc"]

OpusBitstreamFormat = Literal["opus", "ogg"]

HardwareAcceleration = Literal["no-preference", "prefer-hardware", "prefer-software"]

AlphaOption = Literal["keep", "discard"]

LatencyMode = Literal["quality", "realtime"]

CodecState = Literal["unconfigured", "configured", "closed"]

EncodedAudioChunkType = Literal["key", "delta"]

EncodedVideoChunkType = Literal["key", "delta"]

AudioSampleFormat = Literal["u8", "s16", "s32", "f32", "u8-planar", "s16-planar", "s32-planar", "f32-planar"]

VideoPixelFormat = Literal["I420", "I420A", "I422", "I444", "NV12", "RGBA", "RGBX", "BGRA", "BGRX"]

VideoColorPrimaries = Literal["bt709", "bt470bg", "smpte170m", "bt2020", "smpte432"]

VideoTransferCharacteristics = Literal["bt709", "smpte170m", "iec61966-2-1", "linear", "pq", "hlg"]

VideoMatrixCoefficients = Literal["rgb", "bt709", "bt470bg", "smpte170m", "bt2020-ncl"]

WebGLPowerPreference = Literal["default", "low-power", "high-performance"]

GPUPowerPreference = Literal["low-power", "high-performance"]

GPUFeatureName = Literal["depth-clip-control", "depth32float-stencil8", "texture-compression-bc", "texture-compression-etc2", "texture-compression-astc", "timestamp-query", "indirect-first-instance", "shader-f16", "rg11b10ufloat-renderable"]

GPUBufferMapState = Literal["unmapped", "pending", "mapped"]

GPUTextureDimension = Literal["1d", "2d", "3d"]

GPUTextureViewDimension = Literal["1d", "2d", "2d-array", "cube", "cube-array", "3d"]

GPUTextureAspect = Literal["all", "stencil-only", "depth-only"]

GPUTextureFormat = Literal["r8unorm", "r8snorm", "r8uint", "r8sint", "r16uint", "r16sint", "r16float", "rg8unorm", "rg8snorm", "rg8uint", "rg8sint", "r32uint", "r32sint", "r32float", "rg16uint", "rg16sint", "rg16float", "rgba8unorm", "rgba8unorm-srgb", "rgba8snorm", "rgba8uint", "rgba8sint", "bgra8unorm", "bgra8unorm-srgb", "rgb9e5ufloat", "rgb10a2unorm", "rg11b10ufloat", "rg32uint", "rg32sint", "rg32float", "rgba16uint", "rgba16sint", "rgba16float", "rgba32uint", "rgba32sint", "rgba32float", "stencil8", "depth16unorm", "depth24plus", "depth24plus-stencil8", "depth32float", "depth32float-stencil8", "bc1-rgba-unorm", "bc1-rgba-unorm-srgb", "bc2-rgba-unorm", "bc2-rgba-unorm-srgb", "bc3-rgba-unorm", "bc3-rgba-unorm-srgb", "bc4-r-unorm", "bc4-r-snorm", "bc5-rg-unorm", "bc5-rg-snorm", "bc6h-rgb-ufloat", "bc6h-rgb-float", "bc7-rgba-unorm", "bc7-rgba-unorm-srgb", "etc2-rgb8unorm", "etc2-rgb8unorm-srgb", "etc2-rgb8a1unorm", "etc2-rgb8a1unorm-srgb", "etc2-rgba8unorm", "etc2-rgba8unorm-srgb", "eac-r11unorm", "eac-r11snorm", "eac-rg11unorm", "eac-rg11snorm", "astc-4x4-unorm", "astc-4x4-unorm-srgb", "astc-5x4-unorm", "astc-5x4-unorm-srgb", "astc-5x5-unorm", "astc-5x5-unorm-srgb", "astc-6x5-unorm", "astc-6x5-unorm-srgb", "astc-6x6-unorm", "astc-6x6-unorm-srgb", "astc-8x5-unorm", "astc-8x5-unorm-srgb", "astc-8x6-unorm", "astc-8x6-unorm-srgb", "astc-8x8-unorm", "astc-8x8-unorm-srgb", "astc-10x5-unorm", "astc-10x5-unorm-srgb", "astc-10x6-unorm", "astc-10x6-unorm-srgb", "astc-10x8-unorm", "astc-10x8-unorm-srgb", "astc-10x10-unorm", "astc-10x10-unorm-srgb", "astc-12x10-unorm", "astc-12x10-unorm-srgb", "astc-12x12-unorm", "astc-12x12-unorm-srgb"]

GPUAddressMode = Literal["clamp-to-edge", "repeat", "mirror-repeat"]

GPUFilterMode = Literal["nearest", "linear"]

GPUMipmapFilterMode = Literal["nearest", "linear"]

GPUCompareFunction = Literal["never", "less", "equal", "less-equal", "greater", "not-equal", "greater-equal", "always"]

GPUBufferBindingType = Literal["uniform", "storage", "read-only-storage"]

GPUSamplerBindingType = Literal["filtering", "non-filtering", "comparison"]

GPUTextureSampleType = Literal["float", "unfilterable-float", "depth", "sint", "uint"]

GPUStorageTextureAccess = Literal["write-only"]

GPUCompilationMessageType = Literal["error", "warning", "info"]

GPUPipelineErrorReason = Literal["validation", "internal"]

GPUAutoLayoutMode = Literal["auto"]

GPUPrimitiveTopology = Literal["point-list", "line-list", "line-strip", "triangle-list", "triangle-strip"]

GPUFrontFace = Literal["ccw", "cw"]

GPUCullMode = Literal["none", "front", "back"]

GPUBlendFactor = Literal["zero", "one", "src", "one-minus-src", "src-alpha", "one-minus-src-alpha", "dst", "one-minus-dst", "dst-alpha", "one-minus-dst-alpha", "src-alpha-saturated", "constant", "one-minus-constant"]

GPUBlendOperation = Literal["add", "subtract", "reverse-subtract", "min", "max"]

GPUStencilOperation = Literal["keep", "zero", "replace", "invert", "increment-clamp", "decrement-clamp", "increment-wrap", "decrement-wrap"]

GPUIndexFormat = Literal["uint16", "uint32"]

GPUVertexFormat = Literal["uint8x2", "uint8x4", "sint8x2", "sint8x4", "unorm8x2", "unorm8x4", "snorm8x2", "snorm8x4", "uint16x2", "uint16x4", "sint16x2", "sint16x4", "unorm16x2", "unorm16x4", "snorm16x2", "snorm16x4", "float16x2", "float16x4", "float32", "float32x2", "float32x3", "float32x4", "uint32", "uint32x2", "uint32x3", "uint32x4", "sint32", "sint32x2", "sint32x3", "sint32x4"]

GPUVertexStepMode = Literal["vertex", "instance"]

GPUComputePassTimestampLocation = Literal["beginning", "end"]

GPURenderPassTimestampLocation = Literal["beginning", "end"]

GPULoadOp = Literal["load", "clear"]

GPUStoreOp = Literal["store", "discard"]

GPUQueryType = Literal["occlusion", "timestamp"]

GPUCanvasAlphaMode = Literal["opaque", "premultiplied"]

GPUDeviceLostReason = Literal["destroyed"]

GPUErrorFilter = Literal["validation", "out-of-memory", "internal"]

HIDUnitSystem = Literal["none", "si-linear", "si-rotation", "english-linear", "english-rotation", "vendor-defined", "reserved"]

MIDIPortType = Literal["input", "output"]

MIDIPortDeviceState = Literal["disconnected", "connected"]

MIDIPortConnectionState = Literal["open", "closed", "pending"]

MLDeviceType = Literal["cpu", "gpu"]

MLPowerPreference = Literal["default", "high-performance", "low-power"]

MLInputOperandLayout = Literal["nchw", "nhwc"]

MLOperandType = Literal["float32", "float16", "int32", "uint32", "int8", "uint8"]

MLConv2dFilterOperandLayout = Literal["oihw", "hwio", "ohwi", "ihwo"]

MLAutoPad = Literal["explicit", "same-upper", "same-lower"]

MLConvTranspose2dFilterOperandLayout = Literal["iohw", "hwoi", "ohwi"]

MLGruWeightLayout = Literal["zrn", "rzn"]

MLRecurrentNetworkDirection = Literal["forward", "backward", "both"]

MLLstmWeightLayout = Literal["iofg", "ifgo"]

MLPaddingMode = Literal["constant", "edge", "reflection", "symmetric"]

MLRoundingType = Literal["floor", "ceil"]

MLInterpolationMode = Literal["nearest-neighbor", "linear"]

SFrameTransformRole = Literal["encrypt", "decrypt"]

SFrameTransformErrorEventType = Literal["authentication", "keyID", "syntax"]

RTCEncodedVideoFrameType = Literal["empty", "key", "delta"]

RTCErrorDetailTypeIdp = Literal["idp-bad-script-failure", "idp-execution-failure", "idp-load-failure", "idp-need-login", "idp-timeout", "idp-tls-failure", "idp-token-expired", "idp-token-invalid"]

RTCPriorityType = Literal["very-low", "low", "medium", "high"]

RTCStatsType = Literal["codec", "inbound-rtp", "outbound-rtp", "remote-inbound-rtp", "remote-outbound-rtp", "media-source", "media-playout", "peer-connection", "data-channel", "stream", "track", "transport", "candidate-pair", "local-candidate", "remote-candidate", "certificate"]

RTCQualityLimitationReason = Literal["none", "cpu", "bandwidth", "other"]

RTCDtlsRole = Literal["client", "server", "unknown"]

RTCStatsIceCandidatePairState = Literal["frozen", "waiting", "in-progress", "failed", "succeeded"]

RTCIceTransportPolicy = Literal["relay", "all"]

RTCBundlePolicy = Literal["balanced", "max-compat", "max-bundle"]

RTCRtcpMuxPolicy = Literal["require"]

RTCSignalingState = Literal["stable", "have-local-offer", "have-remote-offer", "have-local-pranswer", "have-remote-pranswer", "closed"]

RTCIceGatheringState = Literal["new", "gathering", "complete"]

RTCPeerConnectionState = Literal["closed", "failed", "disconnected", "new", "connecting", "connected"]

RTCIceConnectionState = Literal["closed", "failed", "disconnected", "new", "checking", "completed", "connected"]

RTCSdpType = Literal["offer", "pranswer", "answer", "rollback"]

RTCIceProtocol = Literal["udp", "tcp"]

RTCIceTcpCandidateType = Literal["active", "passive", "so"]

RTCIceCandidateType = Literal["host", "srflx", "prflx", "relay"]

RTCIceServerTransportProtocol = Literal["udp", "tcp", "tls"]

RTCRtpTransceiverDirection = Literal["sendrecv", "sendonly", "recvonly", "inactive", "stopped"]

RTCDtlsTransportState = Literal["new", "connecting", "connected", "closed", "failed"]

RTCIceGathererState = Literal["new", "gathering", "complete"]

RTCIceTransportState = Literal["new", "checking", "connected", "completed", "disconnected", "failed", "closed"]

RTCIceRole = Literal["unknown", "controlling", "controlled"]

RTCIceComponent = Literal["rtp", "rtcp"]

RTCSctpTransportState = Literal["connecting", "connected", "closed"]

RTCDataChannelState = Literal["connecting", "open", "closing", "closed"]

RTCErrorDetailType = Literal["data-channel-failure", "dtls-failure", "fingerprint-failure", "sctp-failure", "sdp-syntax-error", "hardware-encoder-not-available", "hardware-encoder-error"]

BinaryType = Literal["blob", "arraybuffer"]

WebTransportReliabilityMode = Literal["pending", "reliable-only", "supports-unreliable"]

WebTransportCongestionControl = Literal["default", "throughput", "low-latency"]

WebTransportErrorSource = Literal["stream", "session"]

USBTransferStatus = Literal["ok", "stall", "babble"]

USBRequestType = Literal["standard", "class", "vendor"]

USBRecipient = Literal["device", "interface", "endpoint", "other"]

USBDirection = Literal["in", "out"]

USBEndpointType = Literal["bulk", "interrupt", "isochronous"]

AutoKeyword = Literal["auto"]

DirectionSetting = Literal["", "rl", "lr"]

LineAlignSetting = Literal["start", "center", "end"]

PositionAlignSetting = Literal["line-left", "center", "line-right", "auto"]

AlignSetting = Literal["start", "center", "end", "left", "right"]

ScrollSetting = Literal["", "up"]

XREnvironmentBlendMode = Literal["opaque", "alpha-blend", "additive"]

XRInteractionMode = Literal["screen-space", "world-space"]

XRDepthUsage = Literal["cpu-optimized", "gpu-optimized"]

XRDepthDataFormat = Literal["luminance-alpha", "float32"]

XRDOMOverlayType = Literal["screen", "floating", "head-locked"]

XRHandJoint = Literal["wrist", "thumb-metacarpal", "thumb-phalanx-proximal", "thumb-phalanx-distal", "thumb-tip", "index-finger-metacarpal", "index-finger-phalanx-proximal", "index-finger-phalanx-intermediate", "index-finger-phalanx-distal", "index-finger-tip", "middle-finger-metacarpal", "middle-finger-phalanx-proximal", "middle-finger-phalanx-intermediate", "middle-finger-phalanx-distal", "middle-finger-tip", "ring-finger-metacarpal", "ring-finger-phalanx-proximal", "ring-finger-phalanx-intermediate", "ring-finger-phalanx-distal", "ring-finger-tip", "pinky-finger-metacarpal", "pinky-finger-phalanx-proximal", "pinky-finger-phalanx-intermediate", "pinky-finger-phalanx-distal", "pinky-finger-tip"]

XRHitTestTrackableType = Literal["point", "plane", "mesh"]

XRReflectionFormat = Literal["srgba8", "rgba16f"]

XRSessionMode = Literal["inline", "immersive-vr", "immersive-ar"]

XRVisibilityState = Literal["visible", "visible-blurred", "hidden"]

XRReferenceSpaceType = Literal["viewer", "local", "local-floor", "bounded-floor", "unbounded"]

XREye = Literal["none", "left", "right"]

XRHandedness = Literal["none", "left", "right"]

XRTargetRayMode = Literal["gaze", "tracked-pointer", "screen"]

XRLayerLayout = Literal["default", "mono", "stereo", "stereo-left-right", "stereo-top-bottom"]

XRTextureType = Literal["texture", "texture-array"]

XMLHttpRequestResponseType = Literal["", "arraybuffer", "blob", "document", "json", "text"]

GLuint64EXT = int

BlobPart = BufferSource | Blob | USVString

AlgorithmIdentifier = object | str

HashAlgorithmIdentifier = AlgorithmIdentifier

BigInteger = Uint8Array

NamedCurve = str

ClipboardItemData = Awaitable[str | Blob]

ClipboardItems = Sequence[ClipboardItem]

CookieList = Sequence[CookieListItem]

PasswordCredentialInit = PasswordCredentialData | HTMLFormElement

BinaryData = ArrayBuffer | ArrayBufferView

CSSStringSource = str | ReadableStream

CSSToken = str | CSSStyleValue | CSSParserValue

CSSUnparsedSegment = USVString | CSSVariableReferenceValue

CSSKeywordish = str | CSSKeywordValue

CSSNumberish = float | CSSNumericValue

CSSPerspectiveValue = CSSNumericValue | CSSKeywordish

CSSColorRGBComp = CSSNumberish | CSSKeywordish

CSSColorPercent = CSSNumberish | CSSKeywordish

CSSColorNumber = CSSNumberish | CSSKeywordish

CSSColorAngle = CSSNumberish | CSSKeywordish

GeometryNode = Text | Element | CSSPseudoElement | Document

HeadersInit = Sequence[Sequence[ByteString]] | ByteString

XMLHttpRequestBodyInit = Blob | BufferSource | FormData | URLSearchParams | USVString

BodyInit = ReadableStream | XMLHttpRequestBodyInit

RequestInfo = Request | USVString

StartInDirectory = WellKnownDirectory | FileSystemHandle

FileSystemWriteChunkType = BufferSource | Blob | USVString | WriteParams

DOMHighResTimeStamp = float

EpochTimeStamp = int

HTMLOrSVGScriptElement = HTMLScriptElement | SVGScriptElement

MediaProvider = MediaStream | MediaSource | Blob

RenderingContext = CanvasRenderingContext2D | ImageBitmapRenderingContext | WebGLRenderingContext | WebGL2RenderingContext | GPUCanvasContext

HTMLOrSVGImageElement = HTMLImageElement | SVGImageElement

CanvasImageSource = HTMLOrSVGImageElement | HTMLVideoElement | HTMLCanvasElement | ImageBitmap | OffscreenCanvas | VideoFrame

OffscreenRenderingContext = OffscreenCanvasRenderingContext2D | ImageBitmapRenderingContext | WebGLRenderingContext | WebGL2RenderingContext | GPUCanvasContext

EventHandler = EventHandlerNonNull | None

OnErrorEventHandler = OnErrorEventHandlerNonNull | None

OnBeforeUnloadEventHandler = OnBeforeUnloadEventHandlerNonNull | None

TimerHandler = str | Function

ImageBitmapSource = CanvasImageSource | Blob | ImageData

MessageEventSource = WindowProxy | MessagePort | ServiceWorker

ConstrainPoint2D = Sequence[Point2D] | ConstrainPoint2DParameters

ProfilerResource = str

JsonLdRecord = Any

JsonLdInput = JsonLdRecord | Sequence[JsonLdRecord] | USVString | RemoteDocument

JsonLdContext = JsonLdRecord | Sequence[JsonLdRecord | USVString] | USVString

ConstrainULong = int | ConstrainULongRange

ConstrainDouble = float | ConstrainDoubleRange

ConstrainBoolean = bool | ConstrainBooleanParameters

ConstrainDOMString = str | Sequence[str] | ConstrainDOMStringParameters

Megabit = float

Millisecond = int

RotationMatrixType = Float32Array | Float64Array | DOMMatrix

PerformanceEntryList = Sequence[PerformanceEntry]

PushMessageDataInit = BufferSource | USVString

ReportList = Sequence[Report]

AttributeMatchList = Sequence[str]

ReadableStreamReader = ReadableStreamDefaultReader | ReadableStreamBYOBReader

ReadableStreamController = ReadableStreamDefaultController | ReadableByteStreamController

HTMLString = str

ScriptString = str

ScriptURLString = USVString

TrustedType = TrustedHTML | TrustedScript | TrustedScriptURL

URLPatternInput = USVString | URLPatternInit

VibratePattern = int | Sequence[int]

UUID = str

BluetoothServiceUUID = str | int

BluetoothCharacteristicUUID = str | int

BluetoothDescriptorUUID = str | int

NDEFMessageSource = str | BufferSource | NDEFMessageInit

Base64URLString = str

PublicKeyCredentialJSON = RegistrationResponseJSON | AuthenticationResponseJSON

COSEAlgorithmIdentifier = int

UvmEntry = Sequence[int]

UvmEntries = Sequence[UvmEntry]

ImageBufferSource = BufferSource | ReadableStream

GLenum = int

GLboolean = bool

GLbitfield = int

GLbyte = byte

GLshort = short

GLint = int

GLsizei = int

GLintptr = int

GLsizeiptr = int

GLubyte = octet

GLushort = int

GLuint = int

GLfloat = float

GLclampf = float

TexImageSource = ImageBitmap | ImageData | HTMLImageElement | HTMLCanvasElement | HTMLVideoElement | OffscreenCanvas | VideoFrame

Float32List = Float32Array | Sequence[GLfloat]

Int32List = Int32Array | Sequence[GLint]

GLint64 = int

GLuint64 = int

Uint32List = Uint32Array | Sequence[GLuint]

GPUBufferUsageFlags = int

GPUMapModeFlags = int

GPUTextureUsageFlags = int

GPUShaderStageFlags = int

GPUBindingResource = GPUSampler | GPUTextureView | GPUBufferBinding | GPUExternalTexture

GPUPipelineConstantValue = float

GPUColorWriteFlags = int

GPUComputePassTimestampWrites = Sequence[GPUComputePassTimestampWrite]

GPURenderPassTimestampWrites = Sequence[GPURenderPassTimestampWrite]

GPUBufferDynamicOffset = int

GPUStencilValue = int

GPUSampleMask = int

GPUDepthBias = int

GPUSize64 = int

GPUIntegerCoordinate = int

GPUIndex32 = int

GPUSize32 = int

GPUSignedOffset32 = int

GPUFlagsConstant = int

GPUColor = Sequence[float] | GPUColorDict

GPUOrigin2D = Sequence[GPUIntegerCoordinate] | GPUOrigin2DDict

GPUOrigin3D = Sequence[GPUIntegerCoordinate] | GPUOrigin3DDict

GPUExtent3D = Sequence[GPUIntegerCoordinate] | GPUExtent3DDict

ArrayBufferView = Int8Array | Int16Array | Int32Array | Uint8Array | Uint16Array | Uint32Array | Uint8ClampedArray | BigInt64Array | BigUint64Array | Float32Array | Float64Array | DataView

BufferSource = ArrayBufferView | ArrayBuffer

DOMTimeStamp = int

MLNamedArrayBufferViews = ArrayBufferView

MLGPUResource = GPUBuffer | GPUTexture

MLNamedGPUResources = MLGPUResource

MLNamedOperands = MLOperand

MLBufferView = ArrayBufferView | MLBufferResourceView

RTCRtpTransform = SFrameTransform | RTCRtpScriptTransform

SmallCryptoKeyID = int

CryptoKeyID = SmallCryptoKeyID | bigint

LineAndPositionSetting = float | AutoKeyword

XRWebGLRenderingContext = WebGLRenderingContext | WebGL2RenderingContext

FormDataEntryValue = File | USVString

class ANGLE_instanced_arrays:
    VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE = 0x88FE
    def drawArraysInstancedANGLE(self, mode: GLenum, first: GLint, count: GLsizei, primcount: GLsizei): ...
    def drawElementsInstancedANGLE(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, primcount: GLsizei): ...
    def vertexAttribDivisorANGLE(self, index: GLuint, divisor: GLuint): ...

class CSPViolationReportBody(ReportBody):
    def toJSON(self) -> object: ...
    documentURL: USVString
    referrer: USVString | None
    blockedURL: USVString | None
    effectiveDirective: str
    originalPolicy: str
    sourceFile: USVString | None
    sample: str | None
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: int | None
    columnNumber: int | None

class SecurityPolicyViolationEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: SecurityPolicyViolationEventInit | None = {}) -> SecurityPolicyViolationEvent: ...
    documentURI: USVString
    referrer: USVString
    blockedURI: USVString
    effectiveDirective: str
    violatedDirective: str
    originalPolicy: str
    sourceFile: USVString
    sample: str
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: int
    columnNumber: int

class SecurityPolicyViolationEventInit(TypedDict, EventInit):
    documentURI: USVString
    referrer: NotRequired[USVString]
    blockedURI: NotRequired[USVString]
    violatedDirective: str
    effectiveDirective: str
    originalPolicy: str
    sourceFile: NotRequired[USVString]
    sample: NotRequired[str]
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: NotRequired[int]
    columnNumber: NotRequired[int]

class XMLSerializer:
    @classmethod
    def new(self) -> XMLSerializer: ...
    def serializeToString(self, root: Node) -> str: ...

class InnerHTML:
    innerHTML: str

class Element(Node, InnerHTML, Region, GeometryUtils, ParentNode, NonDocumentTypeChildNode, ChildNode, Slottable, ARIAMixin, Animatable):
    outerHTML: str
    def insertAdjacentHTML(self, position: str, text: str): ...
    def getSpatialNavigationContainer(self) -> Node: ...
    def focusableAreas(self, option: FocusableAreasOption | None = {}) -> Sequence[Node]: ...
    def spatialNavigationSearch(self, dir: SpatialNavigationDirection, options: SpatialNavigationSearchOptions | None = {}) -> Node | None: ...
    def pseudo(self, type: CSSOMString) -> CSSPseudoElement | None: ...
    part: DOMTokenList
    def computedStyleMap(self) -> StylePropertyMapReadOnly: ...
    def getClientRects(self) -> DOMRectList: ...
    def getBoundingClientRect(self) -> DOMRect: ...
    def checkVisibility(self, options: CheckVisibilityOptions | None = {}) -> bool: ...
    def scrollIntoView(self, arg: bool | ScrollIntoViewOptions | None = {}): ...
    @overload
    def scroll(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scroll(self, x: float, y: float): ...
    @overload
    def scrollTo(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollTo(self, x: float, y: float): ...
    @overload
    def scrollBy(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollBy(self, x: float, y: float): ...
    scrollTop: float
    scrollLeft: float
    scrollWidth: int
    scrollHeight: int
    clientTop: int
    clientLeft: int
    clientWidth: int
    clientHeight: int
    namespaceURI: str | None
    prefix: str | None
    localName: str
    tagName: str
    id: str
    className: str
    classList: DOMTokenList
    slot: str
    def hasAttributes(self) -> bool: ...
    attributes: NamedNodeMap
    def getAttributeNames(self) -> Sequence[str]: ...
    def getAttribute(self, qualifiedName: str) -> str | None: ...
    def getAttributeNS(self, namespace: str | None, localName: str) -> str | None: ...
    def setAttribute(self, qualifiedName: str, value: str): ...
    def setAttributeNS(self, namespace: str | None, qualifiedName: str, value: str): ...
    def removeAttribute(self, qualifiedName: str): ...
    def removeAttributeNS(self, namespace: str | None, localName: str): ...
    def toggleAttribute(self, qualifiedName: str, force: bool | None = None) -> bool: ...
    def hasAttribute(self, qualifiedName: str) -> bool: ...
    def hasAttributeNS(self, namespace: str | None, localName: str) -> bool: ...
    def getAttributeNode(self, qualifiedName: str) -> Attr | None: ...
    def getAttributeNodeNS(self, namespace: str | None, localName: str) -> Attr | None: ...
    def setAttributeNode(self, attr: Attr) -> Attr | None: ...
    def setAttributeNodeNS(self, attr: Attr) -> Attr | None: ...
    def removeAttributeNode(self, attr: Attr) -> Attr: ...
    def attachShadow(self, init: ShadowRootInit) -> ShadowRoot: ...
    shadowRoot: ShadowRoot | None
    def closest(self, selectors: str) -> Element | None: ...
    def matches(self, selectors: str) -> bool: ...
    def webkitMatchesSelector(self, selectors: str) -> bool: ...
    def getElementsByTagName(self, qualifiedName: str) -> HTMLCollection: ...
    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...
    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...
    def insertAdjacentElement(self, where: str, element: Element) -> Element | None: ...
    def insertAdjacentText(self, where: str, data: str): ...
    editContext: EditContext | None
    elementTiming: str
    def requestFullscreen(self, options: FullscreenOptions | None = {}) -> Awaitable[None]: ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler
    def setPointerCapture(self, pointerId: int): ...
    def releasePointerCapture(self, pointerId: int): ...
    def hasPointerCapture(self, pointerId: int) -> bool: ...
    def requestPointerLock(self): ...
    def setHTML(self, input: str, options: SetHTMLOptions | None = {}): ...

class ShadowRoot(DocumentFragment, InnerHTML, DocumentOrShadowRoot):
    mode: ShadowRootMode
    delegatesFocus: bool
    slotAssignment: SlotAssignmentMode
    host: Element
    onslotchange: EventHandler

class Range(AbstractRange):
    @classmethod
    def new(self) -> Range: ...
    def createContextualFragment(self, fragment: str) -> DocumentFragment: ...
    def getClientRects(self) -> DOMRectList: ...
    def getBoundingClientRect(self) -> DOMRect: ...
    commonAncestorContainer: Node
    def setStart(self, node: Node, offset: int): ...
    def setEnd(self, node: Node, offset: int): ...
    def setStartBefore(self, node: Node): ...
    def setStartAfter(self, node: Node): ...
    def setEndBefore(self, node: Node): ...
    def setEndAfter(self, node: Node): ...
    def collapse(self, toStart: bool | None = false): ...
    def selectNode(self, node: Node): ...
    def selectNodeContents(self, node: Node): ...
    START_TO_START = 0
    START_TO_END = 1
    END_TO_END = 2
    END_TO_START = 3
    def compareBoundaryPoints(self, how: int, sourceRange: Range) -> short: ...
    def deleteContents(self): ...
    def extractContents(self) -> DocumentFragment: ...
    def cloneContents(self) -> DocumentFragment: ...
    def insertNode(self, node: Node): ...
    def surroundContents(self, newParent: Node): ...
    def cloneRange(self) -> Range: ...
    def detach(self): ...
    def isPointInRange(self, node: Node, offset: int) -> bool: ...
    def comparePoint(self, node: Node, offset: int) -> short: ...
    def intersectsNode(self, node: Node) -> bool: ...

class EXT_blend_minmax:
    MIN_EXT = 0x8007
    MAX_EXT = 0x8008

class EXT_clip_cull_distance:
    MAX_CLIP_DISTANCES_EXT = 0x0D32
    MAX_CULL_DISTANCES_EXT = 0x82F9
    MAX_COMBINED_CLIP_AND_CULL_DISTANCES_EXT = 0x82FA
    CLIP_DISTANCE0_EXT = 0x3000
    CLIP_DISTANCE1_EXT = 0x3001
    CLIP_DISTANCE2_EXT = 0x3002
    CLIP_DISTANCE3_EXT = 0x3003
    CLIP_DISTANCE4_EXT = 0x3004
    CLIP_DISTANCE5_EXT = 0x3005
    CLIP_DISTANCE6_EXT = 0x3006
    CLIP_DISTANCE7_EXT = 0x3007

class EXT_color_buffer_float: ...

class EXT_color_buffer_half_float:
    RGBA16F_EXT = 0x881A
    RGB16F_EXT = 0x881B
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT = 0x8211
    UNSIGNED_NORMALIZED_EXT = 0x8C17

class WebGLTimerQueryEXT(WebGLObject): ...

class EXT_disjoint_timer_query:
    QUERY_COUNTER_BITS_EXT = 0x8864
    CURRENT_QUERY_EXT = 0x8865
    QUERY_RESULT_EXT = 0x8866
    QUERY_RESULT_AVAILABLE_EXT = 0x8867
    TIME_ELAPSED_EXT = 0x88BF
    TIMESTAMP_EXT = 0x8E28
    GPU_DISJOINT_EXT = 0x8FBB
    def createQueryEXT(self) -> WebGLTimerQueryEXT | None: ...
    def deleteQueryEXT(self, query: WebGLTimerQueryEXT | None): ...
    def isQueryEXT(self, query: WebGLTimerQueryEXT | None) -> bool: ...
    def beginQueryEXT(self, target: GLenum, query: WebGLTimerQueryEXT): ...
    def endQueryEXT(self, target: GLenum): ...
    def queryCounterEXT(self, query: WebGLTimerQueryEXT, target: GLenum): ...
    def getQueryEXT(self, target: GLenum, pname: GLenum) -> Any: ...
    def getQueryObjectEXT(self, query: WebGLTimerQueryEXT, pname: GLenum) -> Any: ...

class EXT_disjoint_timer_query_webgl2:
    QUERY_COUNTER_BITS_EXT = 0x8864
    TIME_ELAPSED_EXT = 0x88BF
    TIMESTAMP_EXT = 0x8E28
    GPU_DISJOINT_EXT = 0x8FBB
    def queryCounterEXT(self, query: WebGLQuery, target: GLenum): ...

class EXT_float_blend: ...

class EXT_frag_depth: ...

class EXT_sRGB:
    SRGB_EXT = 0x8C40
    SRGB_ALPHA_EXT = 0x8C42
    SRGB8_ALPHA8_EXT = 0x8C43
    FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT = 0x8210

class EXT_shader_texture_lod: ...

class EXT_texture_compression_bptc:
    COMPRESSED_RGBA_BPTC_UNORM_EXT = 0x8E8C
    COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT = 0x8E8D
    COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT = 0x8E8E
    COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT = 0x8E8F

class EXT_texture_compression_rgtc:
    COMPRESSED_RED_RGTC1_EXT = 0x8DBB
    COMPRESSED_SIGNED_RED_RGTC1_EXT = 0x8DBC
    COMPRESSED_RED_GREEN_RGTC2_EXT = 0x8DBD
    COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT = 0x8DBE

class EXT_texture_filter_anisotropic:
    TEXTURE_MAX_ANISOTROPY_EXT = 0x84FE
    MAX_TEXTURE_MAX_ANISOTROPY_EXT = 0x84FF

class EXT_texture_norm16:
    R16_EXT = 0x822A
    RG16_EXT = 0x822C
    RGB16_EXT = 0x8054
    RGBA16_EXT = 0x805B
    R16_SNORM_EXT = 0x8F98
    RG16_SNORM_EXT = 0x8F99
    RGB16_SNORM_EXT = 0x8F9A
    RGBA16_SNORM_EXT = 0x8F9B

class IdentityProviderWellKnown(TypedDict):
    provider_urls: Sequence[USVString]

class IdentityProviderIcon(TypedDict):
    url: USVString
    size: NotRequired[int]

class IdentityProviderBranding(TypedDict):
    background_color: NotRequired[USVString]
    color: NotRequired[USVString]
    icons: NotRequired[Sequence[IdentityProviderIcon]]

class IdentityProviderAPIConfig(TypedDict):
    accounts_endpoint: USVString
    client_metadata_endpoint: USVString
    id_assertion_endpoint: USVString
    branding: NotRequired[IdentityProviderBranding]

class IdentityProviderAccount(TypedDict):
    id: USVString
    name: USVString
    email: USVString
    given_name: NotRequired[USVString]
    approved_clients: NotRequired[Sequence[USVString]]

class IdentityProviderAccountList(TypedDict):
    accounts: NotRequired[Sequence[IdentityProviderAccount]]

class IdentityProviderClientMetadata(TypedDict):
    privacy_policy_url: NotRequired[USVString]
    terms_of_service_url: NotRequired[USVString]

class IdentityProviderToken(TypedDict):
    token: USVString

class IdentityCredential(Credential):
    token: USVString | None

class CredentialRequestOptions(TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict):
    identity: NotRequired[IdentityCredentialRequestOptions]
    mediation: NotRequired[CredentialMediationRequirement]
    signal: NotRequired[AbortSignal]
    password: NotRequired[bool]
    federated: NotRequired[FederatedCredentialRequestOptions]
    otp: NotRequired[OTPCredentialRequestOptions]
    publicKey: NotRequired[PublicKeyCredentialRequestOptions]

class IdentityCredentialRequestOptions(TypedDict):
    providers: NotRequired[Sequence[IdentityProviderConfig]]

class IdentityProviderConfig(TypedDict):
    configURL: USVString
    clientId: USVString
    nonce: NotRequired[USVString]

class IdentityCredentialLogoutRPsRequest(TypedDict):
    url: USVString
    accountId: USVString

class IdentityProvider: ...

class Blob:
    @classmethod
    def new(self, blobParts: Sequence[BlobPart] | None = None, options: BlobPropertyBag | None = {}) -> Blob: ...
    size: int
    type: str
    def slice(self, start: int | None = None, end: int | None = None, contentType: str | None = None) -> Blob: ...
    def stream(self) -> ReadableStream: ...
    def text(self) -> Awaitable[USVString]: ...
    def arrayBuffer(self) -> Awaitable[ArrayBuffer]: ...

class BlobPropertyBag(TypedDict):
    type: NotRequired[str]
    endings: NotRequired[EndingType]

class File(Blob):
    @classmethod
    def new(self, fileBits: Sequence[BlobPart], fileName: USVString, options: FilePropertyBag | None = {}) -> File: ...
    name: str
    lastModified: int
    webkitRelativePath: USVString

class FilePropertyBag(TypedDict, BlobPropertyBag):
    lastModified: NotRequired[int]

class FileList:
    length: int

class FileReader(EventTarget):
    @classmethod
    def new(self) -> FileReader: ...
    def readAsArrayBuffer(self, blob: Blob): ...
    def readAsBinaryString(self, blob: Blob): ...
    def readAsText(self, blob: Blob, encoding: str | None = None): ...
    def readAsDataURL(self, blob: Blob): ...
    def abort(self): ...
    EMPTY = 0
    LOADING = 1
    DONE = 2
    readyState: int
    result: str | ArrayBuffer | None
    error: DOMException | None
    onloadstart: EventHandler
    onprogress: EventHandler
    onload: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onloadend: EventHandler

class FileReaderSync:
    @classmethod
    def new(self) -> FileReaderSync: ...
    def readAsArrayBuffer(self, blob: Blob) -> ArrayBuffer: ...
    def readAsBinaryString(self, blob: Blob) -> str: ...
    def readAsText(self, blob: Blob, encoding: str | None = None) -> str: ...
    def readAsDataURL(self, blob: Blob) -> str: ...

class URL:
    @classmethod
    def new(self, url: USVString, base: USVString | None = None) -> URL: ...
    href: USVString
    origin: USVString
    protocol: USVString
    username: USVString
    password: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    searchParams: URLSearchParams
    hash: USVString
    def toJSON(self) -> USVString: ...

class IDBRequest(EventTarget):
    result: Any
    error: DOMException | None
    source: IDBObjectStore | IDBIndex | IDBCursor | None
    transaction: IDBTransaction | None
    readyState: IDBRequestReadyState
    onsuccess: EventHandler
    onerror: EventHandler

class IDBOpenDBRequest(IDBRequest):
    onblocked: EventHandler
    onupgradeneeded: EventHandler

class IDBVersionChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: IDBVersionChangeEventInit | None = {}) -> IDBVersionChangeEvent: ...
    oldVersion: int
    newVersion: int | None

class IDBVersionChangeEventInit(TypedDict, EventInit):
    oldVersion: NotRequired[int]
    newVersion: NotRequired[int | None]

class WindowOrWorkerGlobalScope:
    indexedDB: IDBFactory
    crypto: Crypto
    def fetch(self, input: RequestInfo, init: RequestInit | None = {}) -> Awaitable[Response]: ...
    performance: Performance
    origin: USVString
    isSecureContext: bool
    crossOriginIsolated: bool
    def reportError(self, e: Any): ...
    def btoa(self, data: str) -> str: ...
    def atob(self, data: str) -> ByteString: ...
    def setTimeout(self, handler: TimerHandler, timeout: int | None = 0, *arguments: Any) -> int: ...
    def clearTimeout(self, id: int | None = 0): ...
    def setInterval(self, handler: TimerHandler, timeout: int | None = 0, *arguments: Any) -> int: ...
    def clearInterval(self, id: int | None = 0): ...
    def queueMicrotask(self, callback: VoidFunction): ...
    @overload
    def createImageBitmap(self, image: ImageBitmapSource, options: ImageBitmapOptions | None = {}) -> Awaitable[ImageBitmap]: ...
    @overload
    def createImageBitmap(self, image: ImageBitmapSource, sx: int, sy: int, sw: int, sh: int, options: ImageBitmapOptions | None = {}) -> Awaitable[ImageBitmap]: ...
    def structuredClone(self, value: Any, options: StructuredSerializeOptions | None = {}) -> Any: ...
    scheduler: Scheduler
    caches: CacheStorage
    trustedTypes: TrustedTypePolicyFactory

class IDBFactory:
    def open(self, name: str, version: int | None = None) -> IDBOpenDBRequest: ...
    def deleteDatabase(self, name: str) -> IDBOpenDBRequest: ...
    def databases(self) -> Awaitable[Sequence[IDBDatabaseInfo]]: ...
    def cmp(self, first: Any, second: Any) -> short: ...

class IDBDatabaseInfo(TypedDict):
    name: NotRequired[str]
    version: NotRequired[int]

class IDBDatabase(EventTarget):
    name: str
    version: int
    objectStoreNames: DOMStringList
    def transaction(self, storeNames: str | Sequence[str], mode: IDBTransactionMode | None = "readonly", options: IDBTransactionOptions | None = {}) -> IDBTransaction: ...
    def close(self): ...
    def createObjectStore(self, name: str, options: IDBObjectStoreParameters | None = {}) -> IDBObjectStore: ...
    def deleteObjectStore(self, name: str): ...
    onabort: EventHandler
    onclose: EventHandler
    onerror: EventHandler
    onversionchange: EventHandler

class IDBTransactionOptions(TypedDict):
    durability: NotRequired[IDBTransactionDurability]

class IDBObjectStoreParameters(TypedDict):
    keyPath: NotRequired[str | Sequence[str] | None]
    autoIncrement: NotRequired[bool]

class IDBObjectStore:
    name: str
    keyPath: Any
    indexNames: DOMStringList
    transaction: IDBTransaction
    autoIncrement: bool
    def put(self, value: Any, key: Any | None = None) -> IDBRequest: ...
    def add(self, value: Any, key: Any | None = None) -> IDBRequest: ...
    def delete(self, query: Any) -> IDBRequest: ...
    def clear(self) -> IDBRequest: ...
    def get(self, query: Any) -> IDBRequest: ...
    def getKey(self, query: Any) -> IDBRequest: ...
    def getAll(self, query: Any | None = None, count: int | None = None) -> IDBRequest: ...
    def getAllKeys(self, query: Any | None = None, count: int | None = None) -> IDBRequest: ...
    def count(self, query: Any | None = None) -> IDBRequest: ...
    def openCursor(self, query: Any | None = None, direction: IDBCursorDirection | None = "next") -> IDBRequest: ...
    def openKeyCursor(self, query: Any | None = None, direction: IDBCursorDirection | None = "next") -> IDBRequest: ...
    def index(self, name: str) -> IDBIndex: ...
    def createIndex(self, name: str, keyPath: str | Sequence[str], options: IDBIndexParameters | None = {}) -> IDBIndex: ...
    def deleteIndex(self, name: str): ...

class IDBIndexParameters(TypedDict):
    unique: NotRequired[bool]
    multiEntry: NotRequired[bool]

class IDBIndex:
    name: str
    objectStore: IDBObjectStore
    keyPath: Any
    multiEntry: bool
    unique: bool
    def get(self, query: Any) -> IDBRequest: ...
    def getKey(self, query: Any) -> IDBRequest: ...
    def getAll(self, query: Any | None = None, count: int | None = None) -> IDBRequest: ...
    def getAllKeys(self, query: Any | None = None, count: int | None = None) -> IDBRequest: ...
    def count(self, query: Any | None = None) -> IDBRequest: ...
    def openCursor(self, query: Any | None = None, direction: IDBCursorDirection | None = "next") -> IDBRequest: ...
    def openKeyCursor(self, query: Any | None = None, direction: IDBCursorDirection | None = "next") -> IDBRequest: ...

class IDBKeyRange:
    lower: Any
    upper: Any
    lowerOpen: bool
    upperOpen: bool
    def includes(self, key: Any) -> bool: ...

class IDBCursor:
    source: IDBObjectStore | IDBIndex
    direction: IDBCursorDirection
    key: Any
    primaryKey: Any
    request: IDBRequest
    def advance(self, count: int): ...
    def continue_(self, key: Any | None = None): ...
    def continuePrimaryKey(self, key: Any, primaryKey: Any): ...
    def update(self, value: Any) -> IDBRequest: ...
    def delete(self) -> IDBRequest: ...

class IDBCursorWithValue(IDBCursor):
    value: Any

class IDBTransaction(EventTarget):
    objectStoreNames: DOMStringList
    mode: IDBTransactionMode
    durability: IDBTransactionDurability
    db: IDBDatabase
    error: DOMException | None
    def objectStore(self, name: str) -> IDBObjectStore: ...
    def commit(self): ...
    def abort(self): ...
    onabort: EventHandler
    oncomplete: EventHandler
    onerror: EventHandler

class KHR_parallel_shader_compile:
    COMPLETION_STATUS_KHR = 0x91B1

class OES_draw_buffers_indexed:
    def enableiOES(self, target: GLenum, index: GLuint): ...
    def disableiOES(self, target: GLenum, index: GLuint): ...
    def blendEquationiOES(self, buf: GLuint, mode: GLenum): ...
    def blendEquationSeparateiOES(self, buf: GLuint, modeRGB: GLenum, modeAlpha: GLenum): ...
    def blendFunciOES(self, buf: GLuint, src: GLenum, dst: GLenum): ...
    def blendFuncSeparateiOES(self, buf: GLuint, srcRGB: GLenum, dstRGB: GLenum, srcAlpha: GLenum, dstAlpha: GLenum): ...
    def colorMaskiOES(self, buf: GLuint, r: GLboolean, g: GLboolean, b: GLboolean, a: GLboolean): ...

class OES_element_index_uint: ...

class OES_fbo_render_mipmap: ...

class OES_standard_derivatives:
    FRAGMENT_SHADER_DERIVATIVE_HINT_OES = 0x8B8B

class OES_texture_float: ...

class OES_texture_float_linear: ...

class OES_texture_half_float:
    HALF_FLOAT_OES = 0x8D61

class OES_texture_half_float_linear: ...

class WebGLVertexArrayObjectOES(WebGLObject): ...

class OES_vertex_array_object:
    VERTEX_ARRAY_BINDING_OES = 0x85B5
    def createVertexArrayOES(self) -> WebGLVertexArrayObjectOES | None: ...
    def deleteVertexArrayOES(self, arrayObject: WebGLVertexArrayObjectOES | None): ...
    def isVertexArrayOES(self, arrayObject: WebGLVertexArrayObjectOES | None) -> GLboolean: ...
    def bindVertexArrayOES(self, arrayObject: WebGLVertexArrayObjectOES | None): ...

class OVR_multiview2:
    FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR = 0x9630
    FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR = 0x9632
    MAX_VIEWS_OVR = 0x9631
    FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR = 0x9633
    def framebufferTextureMultiviewOVR(self, target: GLenum, attachment: GLenum, texture: WebGLTexture | None, level: GLint, baseViewIndex: GLint, numViews: GLsizei): ...

class SVGElement(Element, GlobalEventHandlers, SVGElementInstance, HTMLOrSVGElement, ElementCSSInlineStyle):
    className: SVGAnimatedString
    ownerSVGElement: SVGSVGElement | None
    viewportElement: SVGElement | None

class SVGBoundingBoxOptions(TypedDict):
    fill: NotRequired[bool]
    stroke: NotRequired[bool]
    markers: NotRequired[bool]
    clipped: NotRequired[bool]

class SVGGraphicsElement(SVGElement, SVGTests):
    transform: SVGAnimatedTransformList
    def getBBox(self, options: SVGBoundingBoxOptions | None = {}) -> DOMRect: ...
    def getCTM(self) -> DOMMatrix | None: ...
    def getScreenCTM(self) -> DOMMatrix | None: ...

class SVGGeometryElement(SVGGraphicsElement):
    pathLength: SVGAnimatedNumber
    def isPointInFill(self, point: DOMPointInit | None = {}) -> bool: ...
    def isPointInStroke(self, point: DOMPointInit | None = {}) -> bool: ...
    def getTotalLength(self) -> float: ...
    def getPointAtLength(self, distance: float) -> DOMPoint: ...

class SVGNumber:
    value: float

class SVGLength:
    SVG_LENGTHTYPE_UNKNOWN = 0
    SVG_LENGTHTYPE_NUMBER = 1
    SVG_LENGTHTYPE_PERCENTAGE = 2
    SVG_LENGTHTYPE_EMS = 3
    SVG_LENGTHTYPE_EXS = 4
    SVG_LENGTHTYPE_PX = 5
    SVG_LENGTHTYPE_CM = 6
    SVG_LENGTHTYPE_MM = 7
    SVG_LENGTHTYPE_IN = 8
    SVG_LENGTHTYPE_PT = 9
    SVG_LENGTHTYPE_PC = 10
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str
    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float): ...
    def convertToSpecifiedUnits(self, unitType: int): ...

class SVGAngle:
    SVG_ANGLETYPE_UNKNOWN = 0
    SVG_ANGLETYPE_UNSPECIFIED = 1
    SVG_ANGLETYPE_DEG = 2
    SVG_ANGLETYPE_RAD = 3
    SVG_ANGLETYPE_GRAD = 4
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str
    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float): ...
    def convertToSpecifiedUnits(self, unitType: int): ...

class SVGNumberList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGNumber) -> SVGNumber: ...
    def insertItemBefore(self, newItem: SVGNumber, index: int) -> SVGNumber: ...
    def replaceItem(self, newItem: SVGNumber, index: int) -> SVGNumber: ...
    def removeItem(self, index: int) -> SVGNumber: ...
    def appendItem(self, newItem: SVGNumber) -> SVGNumber: ...

class SVGLengthList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGLength) -> SVGLength: ...
    def insertItemBefore(self, newItem: SVGLength, index: int) -> SVGLength: ...
    def replaceItem(self, newItem: SVGLength, index: int) -> SVGLength: ...
    def removeItem(self, index: int) -> SVGLength: ...
    def appendItem(self, newItem: SVGLength) -> SVGLength: ...

class SVGStringList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: str) -> str: ...
    def insertItemBefore(self, newItem: str, index: int) -> str: ...
    def replaceItem(self, newItem: str, index: int) -> str: ...
    def removeItem(self, index: int) -> str: ...
    def appendItem(self, newItem: str) -> str: ...

class SVGAnimatedBoolean:
    baseVal: bool
    animVal: bool

class SVGAnimatedEnumeration:
    baseVal: int
    animVal: int

class SVGAnimatedInteger:
    baseVal: int
    animVal: int

class SVGAnimatedNumber:
    baseVal: float
    animVal: float

class SVGAnimatedLength:
    baseVal: SVGLength
    animVal: SVGLength

class SVGAnimatedAngle:
    baseVal: SVGAngle
    animVal: SVGAngle

class SVGAnimatedString:
    baseVal: str
    animVal: str

class SVGAnimatedRect:
    baseVal: DOMRect
    animVal: DOMRectReadOnly

class SVGAnimatedNumberList:
    baseVal: SVGNumberList
    animVal: SVGNumberList

class SVGAnimatedLengthList:
    baseVal: SVGLengthList
    animVal: SVGLengthList

class SVGUnitTypes:
    SVG_UNIT_TYPE_UNKNOWN = 0
    SVG_UNIT_TYPE_USERSPACEONUSE = 1
    SVG_UNIT_TYPE_OBJECTBOUNDINGBOX = 2

class SVGTests:
    requiredExtensions: SVGStringList
    systemLanguage: SVGStringList

class SVGFitToViewBox:
    viewBox: SVGAnimatedRect
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio

class SVGURIReference:
    href: SVGAnimatedString

class Document(Node, FontFaceSource, GeometryUtils, NonElementParentNode, DocumentOrShadowRoot, ParentNode, XPathEvaluatorBase, GlobalEventHandlers):
    @classmethod
    def new(self) -> Document: ...
    rootElement: SVGSVGElement | None
    namedFlows: NamedFlowMap
    def startViewTransition(self, callback: UpdateCallback | None = None) -> ViewTransition: ...
    def elementFromPoint(self, x: float, y: float) -> Element | None: ...
    def elementsFromPoint(self, x: float, y: float) -> Sequence[Element]: ...
    def caretPositionFromPoint(self, x: float, y: float) -> CaretPosition | None: ...
    scrollingElement: Element | None
    implementation: DOMImplementation
    URL: USVString
    documentURI: USVString
    compatMode: str
    characterSet: str
    charset: str
    inputEncoding: str
    contentType: str
    doctype: DocumentType | None
    documentElement: Element | None
    def getElementsByTagName(self, qualifiedName: str) -> HTMLCollection: ...
    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...
    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...
    def createElement(self, localName: str, options: str | ElementCreationOptions | None = {}) -> Element: ...
    def createElementNS(self, namespace: str | None, qualifiedName: str, options: str | ElementCreationOptions | None = {}) -> Element: ...
    def createDocumentFragment(self) -> DocumentFragment: ...
    def createTextNode(self, data: str) -> Text: ...
    def createCDATASection(self, data: str) -> CDATASection: ...
    def createComment(self, data: str) -> Comment: ...
    def createProcessingInstruction(self, target: str, data: str) -> ProcessingInstruction: ...
    def importNode(self, node: Node, deep: bool | None = false) -> Node: ...
    def adoptNode(self, node: Node) -> Node: ...
    def createAttribute(self, localName: str) -> Attr: ...
    def createAttributeNS(self, namespace: str | None, qualifiedName: str) -> Attr: ...
    def createEvent(self, interface: str) -> Event: ...
    def createRange(self) -> Range: ...
    def createNodeIterator(self, root: Node, whatToShow: int | None = 0xFFFFFFFF, filter: NodeFilter | None = None) -> NodeIterator: ...
    def createTreeWalker(self, root: Node, whatToShow: int | None = 0xFFFFFFFF, filter: NodeFilter | None = None) -> TreeWalker: ...
    def measureElement(self, element: Element) -> FontMetrics: ...
    def measureText(self, text: str, styleMap: StylePropertyMapReadOnly) -> FontMetrics: ...
    fullscreenEnabled: bool
    fullscreen: bool
    def exitFullscreen(self) -> Awaitable[None]: ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler
    location: Location | None
    domain: USVString
    referrer: USVString
    cookie: USVString
    lastModified: str
    readyState: DocumentReadyState
    title: str
    dir: str
    body: HTMLElement | None
    head: HTMLHeadElement | None
    images: HTMLCollection
    embeds: HTMLCollection
    plugins: HTMLCollection
    links: HTMLCollection
    forms: HTMLCollection
    scripts: HTMLCollection
    def getElementsByName(self, elementName: str) -> NodeList: ...
    currentScript: HTMLOrSVGScriptElement | None
    @overload
    def open(self, unused1: str | None = None, unused2: str | None = None) -> Document: ...
    @overload
    def open(self, url: USVString, name: str, features: str) -> WindowProxy | None: ...
    def close(self): ...
    def write(self, *text: str): ...
    def writeln(self, *text: str): ...
    defaultView: WindowProxy | None
    def hasFocus(self) -> bool: ...
    designMode: str
    def execCommand(self, commandId: str, showUI: bool | None = false, value: str | None = "") -> bool: ...
    def queryCommandEnabled(self, commandId: str) -> bool: ...
    def queryCommandIndeterm(self, commandId: str) -> bool: ...
    def queryCommandState(self, commandId: str) -> bool: ...
    def queryCommandSupported(self, commandId: str) -> bool: ...
    def queryCommandValue(self, commandId: str) -> str: ...
    hidden: bool
    visibilityState: DocumentVisibilityState
    onreadystatechange: EventHandler
    onvisibilitychange: EventHandler
    fgColor: str
    linkColor: str
    vlinkColor: str
    alinkColor: str
    bgColor: str
    anchors: HTMLCollection
    applets: HTMLCollection
    def clear(self): ...
    def captureEvents(self): ...
    def releaseEvents(self): ...
    all: HTMLAllCollection
    onfreeze: EventHandler
    onresume: EventHandler
    wasDiscarded: bool
    permissionsPolicy: PermissionsPolicy
    pictureInPictureEnabled: bool
    def exitPictureInPicture(self) -> Awaitable[None]: ...
    onpointerlockchange: EventHandler
    onpointerlockerror: EventHandler
    def exitPointerLock(self): ...
    prerendering: bool
    onprerenderingchange: EventHandler
    fragmentDirective: FragmentDirective
    def getSelection(self) -> Selection | None: ...
    def hasStorageAccess(self) -> Awaitable[bool]: ...
    def requestStorageAccess(self) -> Awaitable[None]: ...
    timeline: DocumentTimeline

class SVGSVGElement(SVGGraphicsElement, SVGFitToViewBox, WindowEventHandlers):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    currentScale: float
    currentTranslate: DOMPointReadOnly
    def getIntersectionList(self, rect: DOMRectReadOnly, referenceElement: SVGElement | None) -> NodeList: ...
    def getEnclosureList(self, rect: DOMRectReadOnly, referenceElement: SVGElement | None) -> NodeList: ...
    def checkIntersection(self, element: SVGElement, rect: DOMRectReadOnly) -> bool: ...
    def checkEnclosure(self, element: SVGElement, rect: DOMRectReadOnly) -> bool: ...
    def deselectAll(self): ...
    def createSVGNumber(self) -> SVGNumber: ...
    def createSVGLength(self) -> SVGLength: ...
    def createSVGAngle(self) -> SVGAngle: ...
    def createSVGPoint(self) -> DOMPoint: ...
    def createSVGMatrix(self) -> DOMMatrix: ...
    def createSVGRect(self) -> DOMRect: ...
    def createSVGTransform(self) -> SVGTransform: ...
    def createSVGTransformFromMatrix(self, matrix: DOMMatrix2DInit | None = {}) -> SVGTransform: ...
    def getElementById(self, elementId: str) -> Element: ...
    def suspendRedraw(self, maxWaitMilliseconds: int) -> int: ...
    def unsuspendRedraw(self, suspendHandleID: int): ...
    def unsuspendRedrawAll(self): ...
    def forceRedraw(self): ...
    def pauseAnimations(self): ...
    def unpauseAnimations(self): ...
    def animationsPaused(self) -> bool: ...
    def getCurrentTime(self) -> float: ...
    def setCurrentTime(self, seconds: float): ...

class SVGGElement(SVGGraphicsElement): ...

class SVGDefsElement(SVGGraphicsElement): ...

class SVGDescElement(SVGElement): ...

class SVGMetadataElement(SVGElement): ...

class SVGTitleElement(SVGElement): ...

class SVGSymbolElement(SVGGraphicsElement, SVGFitToViewBox): ...

class SVGUseElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    instanceRoot: SVGElement | None
    animatedInstanceRoot: SVGElement | None

class SVGUseElementShadowRoot(ShadowRoot): ...

class SVGElementInstance:
    correspondingElement: SVGElement | None
    correspondingUseElement: SVGUseElement | None

class ShadowAnimation(Animation):
    @classmethod
    def new(self, source: Animation, newTarget: Element | CSSPseudoElement) -> ShadowAnimation: ...
    sourceAnimation: Animation

class SVGSwitchElement(SVGGraphicsElement): ...

class GetSVGDocument:
    def getSVGDocument(self) -> Document: ...

class SVGStyleElement(SVGElement, LinkStyle):
    type: str
    media: str
    title: str

class SVGTransform:
    SVG_TRANSFORM_UNKNOWN = 0
    SVG_TRANSFORM_MATRIX = 1
    SVG_TRANSFORM_TRANSLATE = 2
    SVG_TRANSFORM_SCALE = 3
    SVG_TRANSFORM_ROTATE = 4
    SVG_TRANSFORM_SKEWX = 5
    SVG_TRANSFORM_SKEWY = 6
    type: int
    matrix: DOMMatrix
    angle: float
    def setMatrix(self, matrix: DOMMatrix2DInit | None = {}): ...
    def setTranslate(self, tx: float, ty: float): ...
    def setScale(self, sx: float, sy: float): ...
    def setRotate(self, angle: float, cx: float, cy: float): ...
    def setSkewX(self, angle: float): ...
    def setSkewY(self, angle: float): ...

class SVGTransformList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGTransform) -> SVGTransform: ...
    def insertItemBefore(self, newItem: SVGTransform, index: int) -> SVGTransform: ...
    def replaceItem(self, newItem: SVGTransform, index: int) -> SVGTransform: ...
    def removeItem(self, index: int) -> SVGTransform: ...
    def appendItem(self, newItem: SVGTransform) -> SVGTransform: ...
    def createSVGTransformFromMatrix(self, matrix: DOMMatrix2DInit | None = {}) -> SVGTransform: ...
    def consolidate(self) -> SVGTransform | None: ...

class SVGAnimatedTransformList:
    baseVal: SVGTransformList
    animVal: SVGTransformList

class SVGPreserveAspectRatio:
    SVG_PRESERVEASPECTRATIO_UNKNOWN = 0
    SVG_PRESERVEASPECTRATIO_NONE = 1
    SVG_PRESERVEASPECTRATIO_XMINYMIN = 2
    SVG_PRESERVEASPECTRATIO_XMIDYMIN = 3
    SVG_PRESERVEASPECTRATIO_XMAXYMIN = 4
    SVG_PRESERVEASPECTRATIO_XMINYMID = 5
    SVG_PRESERVEASPECTRATIO_XMIDYMID = 6
    SVG_PRESERVEASPECTRATIO_XMAXYMID = 7
    SVG_PRESERVEASPECTRATIO_XMINYMAX = 8
    SVG_PRESERVEASPECTRATIO_XMIDYMAX = 9
    SVG_PRESERVEASPECTRATIO_XMAXYMAX = 10
    SVG_MEETORSLICE_UNKNOWN = 0
    SVG_MEETORSLICE_MEET = 1
    SVG_MEETORSLICE_SLICE = 2
    align: int
    meetOrSlice: int

class SVGAnimatedPreserveAspectRatio:
    baseVal: SVGPreserveAspectRatio
    animVal: SVGPreserveAspectRatio

class SVGPathElement(SVGGeometryElement): ...

class SVGRectElement(SVGGeometryElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class SVGCircleElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength

class SVGEllipseElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class SVGLineElement(SVGGeometryElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class SVGAnimatedPoints:
    points: SVGPointList
    animatedPoints: SVGPointList

class SVGPointList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: DOMPoint) -> DOMPoint: ...
    def insertItemBefore(self, newItem: DOMPoint, index: int) -> DOMPoint: ...
    def replaceItem(self, newItem: DOMPoint, index: int) -> DOMPoint: ...
    def removeItem(self, index: int) -> DOMPoint: ...
    def appendItem(self, newItem: DOMPoint) -> DOMPoint: ...

class SVGPolylineElement(SVGGeometryElement, SVGAnimatedPoints): ...

class SVGPolygonElement(SVGGeometryElement, SVGAnimatedPoints): ...

class SVGTextContentElement(SVGGraphicsElement):
    LENGTHADJUST_UNKNOWN = 0
    LENGTHADJUST_SPACING = 1
    LENGTHADJUST_SPACINGANDGLYPHS = 2
    textLength: SVGAnimatedLength
    lengthAdjust: SVGAnimatedEnumeration
    def getNumberOfChars(self) -> int: ...
    def getComputedTextLength(self) -> float: ...
    def getSubStringLength(self, charnum: int, nchars: int) -> float: ...
    def getStartPositionOfChar(self, charnum: int) -> DOMPoint: ...
    def getEndPositionOfChar(self, charnum: int) -> DOMPoint: ...
    def getExtentOfChar(self, charnum: int) -> DOMRect: ...
    def getRotationOfChar(self, charnum: int) -> float: ...
    def getCharNumAtPosition(self, point: DOMPointInit | None = {}) -> int: ...
    def selectSubString(self, charnum: int, nchars: int): ...

class SVGTextPositioningElement(SVGTextContentElement):
    x: SVGAnimatedLengthList
    y: SVGAnimatedLengthList
    dx: SVGAnimatedLengthList
    dy: SVGAnimatedLengthList
    rotate: SVGAnimatedNumberList

class SVGTextElement(SVGTextPositioningElement): ...

class SVGTSpanElement(SVGTextPositioningElement): ...

class SVGTextPathElement(SVGTextContentElement, SVGURIReference):
    TEXTPATH_METHODTYPE_UNKNOWN = 0
    TEXTPATH_METHODTYPE_ALIGN = 1
    TEXTPATH_METHODTYPE_STRETCH = 2
    TEXTPATH_SPACINGTYPE_UNKNOWN = 0
    TEXTPATH_SPACINGTYPE_AUTO = 1
    TEXTPATH_SPACINGTYPE_EXACT = 2
    startOffset: SVGAnimatedLength
    method: SVGAnimatedEnumeration
    spacing: SVGAnimatedEnumeration

class SVGImageElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio
    crossOrigin: str | None

class SVGForeignObjectElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGMarkerElement(SVGElement, SVGFitToViewBox):
    SVG_MARKERUNITS_UNKNOWN = 0
    SVG_MARKERUNITS_USERSPACEONUSE = 1
    SVG_MARKERUNITS_STROKEWIDTH = 2
    SVG_MARKER_ORIENT_UNKNOWN = 0
    SVG_MARKER_ORIENT_AUTO = 1
    SVG_MARKER_ORIENT_ANGLE = 2
    refX: SVGAnimatedLength
    refY: SVGAnimatedLength
    markerUnits: SVGAnimatedEnumeration
    markerWidth: SVGAnimatedLength
    markerHeight: SVGAnimatedLength
    orientType: SVGAnimatedEnumeration
    orientAngle: SVGAnimatedAngle
    orient: str
    def setOrientToAuto(self): ...
    def setOrientToAngle(self, angle: SVGAngle): ...

class SVGGradientElement(SVGElement, SVGURIReference):
    SVG_SPREADMETHOD_UNKNOWN = 0
    SVG_SPREADMETHOD_PAD = 1
    SVG_SPREADMETHOD_REFLECT = 2
    SVG_SPREADMETHOD_REPEAT = 3
    gradientUnits: SVGAnimatedEnumeration
    gradientTransform: SVGAnimatedTransformList
    spreadMethod: SVGAnimatedEnumeration

class SVGLinearGradientElement(SVGGradientElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class SVGRadialGradientElement(SVGGradientElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength
    fx: SVGAnimatedLength
    fy: SVGAnimatedLength
    fr: SVGAnimatedLength

class SVGStopElement(SVGElement):
    offset: SVGAnimatedNumber

class SVGPatternElement(SVGElement, SVGFitToViewBox, SVGURIReference):
    patternUnits: SVGAnimatedEnumeration
    patternContentUnits: SVGAnimatedEnumeration
    patternTransform: SVGAnimatedTransformList
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGScriptElement(SVGElement, SVGURIReference):
    type: str
    crossOrigin: str | None

class SVGAElement(SVGGraphicsElement, SVGURIReference):
    target: SVGAnimatedString
    download: str
    ping: USVString
    rel: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    referrerPolicy: str
    origin: USVString
    protocol: USVString
    username: USVString
    password: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class SVGViewElement(SVGElement, SVGFitToViewBox): ...

class WEBGL_blend_equation_advanced_coherent:
    MULTIPLY = 0x9294
    SCREEN = 0x9295
    OVERLAY = 0x9296
    DARKEN = 0x9297
    LIGHTEN = 0x9298
    COLORDODGE = 0x9299
    COLORBURN = 0x929A
    HARDLIGHT = 0x929B
    SOFTLIGHT = 0x929C
    DIFFERENCE = 0x929E
    EXCLUSION = 0x92A0
    HSL_HUE = 0x92AD
    HSL_SATURATION = 0x92AE
    HSL_COLOR = 0x92AF
    HSL_LUMINOSITY = 0x92B0

class WEBGL_color_buffer_float:
    RGBA32F_EXT = 0x8814
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT = 0x8211
    UNSIGNED_NORMALIZED_EXT = 0x8C17

class WEBGL_compressed_texture_astc:
    COMPRESSED_RGBA_ASTC_4x4_KHR = 0x93B0
    COMPRESSED_RGBA_ASTC_5x4_KHR = 0x93B1
    COMPRESSED_RGBA_ASTC_5x5_KHR = 0x93B2
    COMPRESSED_RGBA_ASTC_6x5_KHR = 0x93B3
    COMPRESSED_RGBA_ASTC_6x6_KHR = 0x93B4
    COMPRESSED_RGBA_ASTC_8x5_KHR = 0x93B5
    COMPRESSED_RGBA_ASTC_8x6_KHR = 0x93B6
    COMPRESSED_RGBA_ASTC_8x8_KHR = 0x93B7
    COMPRESSED_RGBA_ASTC_10x5_KHR = 0x93B8
    COMPRESSED_RGBA_ASTC_10x6_KHR = 0x93B9
    COMPRESSED_RGBA_ASTC_10x8_KHR = 0x93BA
    COMPRESSED_RGBA_ASTC_10x10_KHR = 0x93BB
    COMPRESSED_RGBA_ASTC_12x10_KHR = 0x93BC
    COMPRESSED_RGBA_ASTC_12x12_KHR = 0x93BD
    COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR = 0x93D0
    COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR = 0x93D1
    COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR = 0x93D2
    COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR = 0x93D3
    COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR = 0x93D4
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR = 0x93D5
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR = 0x93D6
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR = 0x93D7
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR = 0x93D8
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR = 0x93D9
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR = 0x93DA
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR = 0x93DB
    COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR = 0x93DC
    COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR = 0x93DD
    def getSupportedProfiles(self) -> Sequence[str]: ...

class WEBGL_compressed_texture_etc:
    COMPRESSED_R11_EAC = 0x9270
    COMPRESSED_SIGNED_R11_EAC = 0x9271
    COMPRESSED_RG11_EAC = 0x9272
    COMPRESSED_SIGNED_RG11_EAC = 0x9273
    COMPRESSED_RGB8_ETC2 = 0x9274
    COMPRESSED_SRGB8_ETC2 = 0x9275
    COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
    COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
    COMPRESSED_RGBA8_ETC2_EAC = 0x9278
    COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279

class WEBGL_compressed_texture_etc1:
    COMPRESSED_RGB_ETC1_WEBGL = 0x8D64

class WEBGL_compressed_texture_pvrtc:
    COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 0x8C00
    COMPRESSED_RGB_PVRTC_2BPPV1_IMG = 0x8C01
    COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 0x8C02
    COMPRESSED_RGBA_PVRTC_2BPPV1_IMG = 0x8C03

class WEBGL_compressed_texture_s3tc:
    COMPRESSED_RGB_S3TC_DXT1_EXT = 0x83F0
    COMPRESSED_RGBA_S3TC_DXT1_EXT = 0x83F1
    COMPRESSED_RGBA_S3TC_DXT3_EXT = 0x83F2
    COMPRESSED_RGBA_S3TC_DXT5_EXT = 0x83F3

class WEBGL_compressed_texture_s3tc_srgb:
    COMPRESSED_SRGB_S3TC_DXT1_EXT = 0x8C4C
    COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT = 0x8C4D
    COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT = 0x8C4E
    COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT = 0x8C4F

class WEBGL_debug_renderer_info:
    UNMASKED_VENDOR_WEBGL = 0x9245
    UNMASKED_RENDERER_WEBGL = 0x9246

class WEBGL_debug_shaders:
    def getTranslatedShaderSource(self, shader: WebGLShader) -> str: ...

class WEBGL_depth_texture:
    UNSIGNED_INT_24_8_WEBGL = 0x84FA

class WEBGL_draw_buffers:
    COLOR_ATTACHMENT0_WEBGL = 0x8CE0
    COLOR_ATTACHMENT1_WEBGL = 0x8CE1
    COLOR_ATTACHMENT2_WEBGL = 0x8CE2
    COLOR_ATTACHMENT3_WEBGL = 0x8CE3
    COLOR_ATTACHMENT4_WEBGL = 0x8CE4
    COLOR_ATTACHMENT5_WEBGL = 0x8CE5
    COLOR_ATTACHMENT6_WEBGL = 0x8CE6
    COLOR_ATTACHMENT7_WEBGL = 0x8CE7
    COLOR_ATTACHMENT8_WEBGL = 0x8CE8
    COLOR_ATTACHMENT9_WEBGL = 0x8CE9
    COLOR_ATTACHMENT10_WEBGL = 0x8CEA
    COLOR_ATTACHMENT11_WEBGL = 0x8CEB
    COLOR_ATTACHMENT12_WEBGL = 0x8CEC
    COLOR_ATTACHMENT13_WEBGL = 0x8CED
    COLOR_ATTACHMENT14_WEBGL = 0x8CEE
    COLOR_ATTACHMENT15_WEBGL = 0x8CEF
    DRAW_BUFFER0_WEBGL = 0x8825
    DRAW_BUFFER1_WEBGL = 0x8826
    DRAW_BUFFER2_WEBGL = 0x8827
    DRAW_BUFFER3_WEBGL = 0x8828
    DRAW_BUFFER4_WEBGL = 0x8829
    DRAW_BUFFER5_WEBGL = 0x882A
    DRAW_BUFFER6_WEBGL = 0x882B
    DRAW_BUFFER7_WEBGL = 0x882C
    DRAW_BUFFER8_WEBGL = 0x882D
    DRAW_BUFFER9_WEBGL = 0x882E
    DRAW_BUFFER10_WEBGL = 0x882F
    DRAW_BUFFER11_WEBGL = 0x8830
    DRAW_BUFFER12_WEBGL = 0x8831
    DRAW_BUFFER13_WEBGL = 0x8832
    DRAW_BUFFER14_WEBGL = 0x8833
    DRAW_BUFFER15_WEBGL = 0x8834
    MAX_COLOR_ATTACHMENTS_WEBGL = 0x8CDF
    MAX_DRAW_BUFFERS_WEBGL = 0x8824
    def drawBuffersWEBGL(self, buffers: Sequence[GLenum]): ...

class WEBGL_draw_instanced_base_vertex_base_instance:
    def drawArraysInstancedBaseInstanceWEBGL(self, mode: GLenum, first: GLint, count: GLsizei, instanceCount: GLsizei, baseInstance: GLuint): ...
    def drawElementsInstancedBaseVertexBaseInstanceWEBGL(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, instanceCount: GLsizei, baseVertex: GLint, baseInstance: GLuint): ...

class WEBGL_lose_context:
    def loseContext(self): ...
    def restoreContext(self): ...

class WEBGL_multi_draw:
    def multiDrawArraysWEBGL(self, mode: GLenum, firstsList: Int32Array | Sequence[GLint], firstsOffset: GLuint, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawElementsWEBGL(self, mode: GLenum, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, type: GLenum, offsetsList: Int32Array | Sequence[GLsizei], offsetsOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawArraysInstancedWEBGL(self, mode: GLenum, firstsList: Int32Array | Sequence[GLint], firstsOffset: GLuint, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawElementsInstancedWEBGL(self, mode: GLenum, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, type: GLenum, offsetsList: Int32Array | Sequence[GLsizei], offsetsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, drawcount: GLsizei): ...

class WEBGL_multi_draw_instanced_base_vertex_base_instance:
    def multiDrawArraysInstancedBaseInstanceWEBGL(self, mode: GLenum, firstsList: Int32Array | Sequence[GLint], firstsOffset: GLuint, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, baseInstancesList: Uint32Array | Sequence[GLuint], baseInstancesOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL(self, mode: GLenum, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, type: GLenum, offsetsList: Int32Array | Sequence[GLsizei], offsetsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, baseVerticesList: Int32Array | Sequence[GLint], baseVerticesOffset: GLuint, baseInstancesList: Uint32Array | Sequence[GLuint], baseInstancesOffset: GLuint, drawcount: GLsizei): ...

class Crypto:
    subtle: SubtleCrypto
    def getRandomValues(self, array: ArrayBufferView) -> ArrayBufferView: ...
    def randomUUID(self) -> str: ...

class Algorithm(TypedDict):
    name: str

class KeyAlgorithm(TypedDict):
    name: str

class CryptoKey:
    type: KeyType
    extractable: bool
    algorithm: object
    usages: object

class SubtleCrypto:
    def encrypt(self, algorithm: AlgorithmIdentifier, key: CryptoKey, data: BufferSource) -> Awaitable[Any]: ...
    def decrypt(self, algorithm: AlgorithmIdentifier, key: CryptoKey, data: BufferSource) -> Awaitable[Any]: ...
    def sign(self, algorithm: AlgorithmIdentifier, key: CryptoKey, data: BufferSource) -> Awaitable[Any]: ...
    def verify(self, algorithm: AlgorithmIdentifier, key: CryptoKey, signature: BufferSource, data: BufferSource) -> Awaitable[Any]: ...
    def digest(self, algorithm: AlgorithmIdentifier, data: BufferSource) -> Awaitable[Any]: ...
    def generateKey(self, algorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[Any]: ...
    def deriveKey(self, algorithm: AlgorithmIdentifier, baseKey: CryptoKey, derivedKeyType: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[Any]: ...
    def deriveBits(self, algorithm: AlgorithmIdentifier, baseKey: CryptoKey, length: int) -> Awaitable[ArrayBuffer]: ...
    def importKey(self, format: KeyFormat, keyData: BufferSource | JsonWebKey, algorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[CryptoKey]: ...
    def exportKey(self, format: KeyFormat, key: CryptoKey) -> Awaitable[Any]: ...
    def wrapKey(self, format: KeyFormat, key: CryptoKey, wrappingKey: CryptoKey, wrapAlgorithm: AlgorithmIdentifier) -> Awaitable[Any]: ...
    def unwrapKey(self, format: KeyFormat, wrappedKey: BufferSource, unwrappingKey: CryptoKey, unwrapAlgorithm: AlgorithmIdentifier, unwrappedKeyAlgorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[CryptoKey]: ...

class RsaOtherPrimesInfo(TypedDict):
    r: NotRequired[str]
    d: NotRequired[str]
    t: NotRequired[str]

class JsonWebKey(TypedDict):
    kty: NotRequired[str]
    use: NotRequired[str]
    key_ops: NotRequired[Sequence[str]]
    alg: NotRequired[str]
    ext: NotRequired[bool]
    crv: NotRequired[str]
    x: NotRequired[str]
    y: NotRequired[str]
    d: NotRequired[str]
    n: NotRequired[str]
    e: NotRequired[str]
    p: NotRequired[str]
    q: NotRequired[str]
    dp: NotRequired[str]
    dq: NotRequired[str]
    qi: NotRequired[str]
    oth: NotRequired[Sequence[RsaOtherPrimesInfo]]
    k: NotRequired[str]

class CryptoKeyPair(TypedDict):
    publicKey: NotRequired[CryptoKey]
    privateKey: NotRequired[CryptoKey]

class RsaKeyGenParams(TypedDict, Algorithm):
    modulusLength: int
    publicExponent: BigInteger

class RsaHashedKeyGenParams(TypedDict, RsaKeyGenParams):
    hash: HashAlgorithmIdentifier

class RsaKeyAlgorithm(TypedDict, KeyAlgorithm):
    modulusLength: int
    publicExponent: BigInteger

class RsaHashedKeyAlgorithm(TypedDict, RsaKeyAlgorithm):
    hash: KeyAlgorithm

class RsaHashedImportParams(TypedDict, Algorithm):
    hash: HashAlgorithmIdentifier

class RsaPssParams(TypedDict, Algorithm):
    saltLength: int

class RsaOaepParams(TypedDict, Algorithm):
    label: NotRequired[BufferSource]

class EcdsaParams(TypedDict, Algorithm):
    hash: HashAlgorithmIdentifier

class EcKeyGenParams(TypedDict, Algorithm):
    namedCurve: NamedCurve

class EcKeyAlgorithm(TypedDict, KeyAlgorithm):
    namedCurve: NamedCurve

class EcKeyImportParams(TypedDict, Algorithm):
    namedCurve: NamedCurve

class EcdhKeyDeriveParams(TypedDict, Algorithm):
    public: CryptoKey

class AesCtrParams(TypedDict, Algorithm):
    counter: BufferSource
    length: octet

class AesKeyAlgorithm(TypedDict, KeyAlgorithm):
    length: int

class AesKeyGenParams(TypedDict, Algorithm):
    length: int

class AesDerivedKeyParams(TypedDict, Algorithm):
    length: int

class AesCbcParams(TypedDict, Algorithm):
    iv: BufferSource

class AesGcmParams(TypedDict, Algorithm):
    iv: BufferSource
    additionalData: NotRequired[BufferSource]
    tagLength: NotRequired[octet]

class HmacImportParams(TypedDict, Algorithm):
    hash: HashAlgorithmIdentifier
    length: NotRequired[int]

class HmacKeyAlgorithm(TypedDict, KeyAlgorithm):
    hash: KeyAlgorithm
    length: int

class HmacKeyGenParams(TypedDict, Algorithm):
    hash: HashAlgorithmIdentifier
    length: NotRequired[int]

class HkdfParams(TypedDict, Algorithm):
    hash: HashAlgorithmIdentifier
    salt: BufferSource
    info: BufferSource

class Pbkdf2Params(TypedDict, Algorithm):
    salt: BufferSource
    iterations: int
    hash: HashAlgorithmIdentifier

class Accelerometer(Sensor):
    @classmethod
    def new(self, options: AccelerometerSensorOptions | None = {}) -> Accelerometer: ...
    x: float | None
    y: float | None
    z: float | None

class AccelerometerSensorOptions(TypedDict, SensorOptions):
    referenceFrame: NotRequired[AccelerometerLocalCoordinateSystem]

class LinearAccelerationSensor(Accelerometer):
    @classmethod
    def new(self, options: AccelerometerSensorOptions | None = {}) -> LinearAccelerationSensor: ...

class GravitySensor(Accelerometer):
    @classmethod
    def new(self, options: AccelerometerSensorOptions | None = {}) -> GravitySensor: ...

class AccelerometerReadingValues(TypedDict):
    x: float | None
    y: float | None
    z: float | None

class LinearAccelerationReadingValues(TypedDict, AccelerometerReadingValues): ...

class GravityReadingValues(TypedDict, AccelerometerReadingValues): ...

class AmbientLightSensor(Sensor):
    @classmethod
    def new(self, sensorOptions: SensorOptions | None = {}) -> AmbientLightSensor: ...
    illuminance: float | None

class AmbientLightReadingValues(TypedDict):
    illuminance: float | None

class XRAnchor:
    anchorSpace: XRSpace
    def requestPersistentHandle(self) -> Awaitable[str]: ...
    def delete(self): ...

class XRFrame:
    def createAnchor(self, pose: XRRigidTransform, space: XRSpace) -> Awaitable[XRAnchor]: ...
    trackedAnchors: XRAnchorSet
    def getDepthInformation(self, view: XRView) -> XRCPUDepthInformation | None: ...
    def getJointPose(self, joint: XRJointSpace, baseSpace: XRSpace) -> XRJointPose | None: ...
    def fillJointRadii(self, jointSpaces: Sequence[XRJointSpace], radii: Float32Array) -> bool: ...
    def fillPoses(self, spaces: Sequence[XRSpace], baseSpace: XRSpace, transforms: Float32Array) -> bool: ...
    def getHitTestResults(self, hitTestSource: XRHitTestSource) -> Sequence[XRHitTestResult]: ...
    def getHitTestResultsForTransientInput(self, hitTestSource: XRTransientInputHitTestSource) -> Sequence[XRTransientInputHitTestResult]: ...
    def getLightEstimate(self, lightProbe: XRLightProbe) -> XRLightEstimate | None: ...
    session: XRSession
    predictedDisplayTime: DOMHighResTimeStamp
    def getViewerPose(self, referenceSpace: XRReferenceSpace) -> XRViewerPose | None: ...
    def getPose(self, space: XRSpace, baseSpace: XRSpace) -> XRPose | None: ...

class XRSession(EventTarget):
    def restorePersistentAnchor(self, uuid: str) -> Awaitable[XRAnchor]: ...
    def deletePersistentAnchor(self, uuid: str) -> Awaitable[None]: ...
    environmentBlendMode: XREnvironmentBlendMode
    interactionMode: XRInteractionMode
    depthUsage: XRDepthUsage
    depthDataFormat: XRDepthDataFormat
    domOverlayState: XRDOMOverlayState | None
    def requestHitTestSource(self, options: XRHitTestOptionsInit) -> Awaitable[XRHitTestSource]: ...
    def requestHitTestSourceForTransientInput(self, options: XRTransientInputHitTestOptionsInit) -> Awaitable[XRTransientInputHitTestSource]: ...
    def requestLightProbe(self, options: XRLightProbeInit | None = {}) -> Awaitable[XRLightProbe]: ...
    preferredReflectionFormat: XRReflectionFormat
    visibilityState: XRVisibilityState
    frameRate: float | None
    supportedFrameRates: Float32Array
    renderState: XRRenderState
    inputSources: XRInputSourceArray
    enabledFeatures: Sequence[str]
    def updateRenderState(self, state: XRRenderStateInit | None = {}): ...
    def updateTargetFrameRate(self, rate: float) -> Awaitable[None]: ...
    def requestReferenceSpace(self, type: XRReferenceSpaceType) -> Awaitable[XRReferenceSpace]: ...
    def requestAnimationFrame(self, callback: XRFrameRequestCallback) -> int: ...
    def cancelAnimationFrame(self, handle: int): ...
    def end(self) -> Awaitable[None]: ...
    onend: EventHandler
    oninputsourceschange: EventHandler
    onselect: EventHandler
    onselectstart: EventHandler
    onselectend: EventHandler
    onsqueeze: EventHandler
    onsqueezestart: EventHandler
    onsqueezeend: EventHandler
    onvisibilitychange: EventHandler
    onframeratechange: EventHandler

class XRHitTestResult:
    def createAnchor(self) -> Awaitable[XRAnchor]: ...
    def getPose(self, baseSpace: XRSpace) -> XRPose | None: ...

class XRAnchorSet: ...

class HTMLAttributionSrcElementUtils:
    attributionSrc: USVString

class HTMLAnchorElement(HTMLElement, HTMLAttributionSrcElementUtils, HTMLHyperlinkElementUtils):
    @classmethod
    def new(self) -> HTMLAnchorElement: ...
    target: str
    download: str
    ping: USVString
    rel: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    referrerPolicy: str
    coords: str
    charset: str
    name: str
    rev: str
    shape: str
    attributionSourceId: int

class HTMLImageElement(HTMLElement, HTMLAttributionSrcElementUtils):
    @classmethod
    def new(self) -> HTMLImageElement: ...
    x: int
    y: int
    """ # GIgnoredStmt 
    LegacyFactoryFunction=Image(optional unsigned long width, optional unsigned long height)
    """
    alt: str
    src: USVString
    srcset: USVString
    sizes: str
    crossOrigin: str | None
    useMap: str
    isMap: bool
    width: int
    height: int
    naturalWidth: int
    naturalHeight: int
    complete: bool
    currentSrc: USVString
    referrerPolicy: str
    decoding: str
    loading: str
    def decode(self) -> Awaitable[None]: ...
    name: str
    lowsrc: USVString
    align: str
    hspace: int
    vspace: int
    longDesc: USVString
    border: str
    fetchPriority: str

class HTMLScriptElement(HTMLElement, HTMLAttributionSrcElementUtils):
    @classmethod
    def new(self) -> HTMLScriptElement: ...
    src: USVString
    type: str
    noModule: bool
    async_: bool
    defer: bool
    crossOrigin: str | None
    text: str
    integrity: str
    referrerPolicy: str
    blocking: DOMTokenList
    charset: str
    event: str
    htmlFor: str
    fetchPriority: str

class HTMLMediaElement(HTMLElement):
    sinkId: str
    def setSinkId(self, sinkId: str) -> Awaitable[None]: ...
    mediaKeys: MediaKeys | None
    onencrypted: EventHandler
    onwaitingforkey: EventHandler
    def setMediaKeys(self, mediaKeys: MediaKeys | None) -> Awaitable[None]: ...
    error: MediaError | None
    src: USVString
    srcObject: MediaProvider | None
    currentSrc: USVString
    crossOrigin: str | None
    NETWORK_EMPTY = 0
    NETWORK_IDLE = 1
    NETWORK_LOADING = 2
    NETWORK_NO_SOURCE = 3
    networkState: int
    preload: str
    buffered: TimeRanges
    def load(self): ...
    def canPlayType(self, type: str) -> CanPlayTypeResult: ...
    HAVE_NOTHING = 0
    HAVE_METADATA = 1
    HAVE_CURRENT_DATA = 2
    HAVE_FUTURE_DATA = 3
    HAVE_ENOUGH_DATA = 4
    readyState: int
    seeking: bool
    currentTime: float
    def fastSeek(self, time: float): ...
    duration: float
    def getStartDate(self) -> object: ...
    paused: bool
    defaultPlaybackRate: float
    playbackRate: float
    preservesPitch: bool
    played: TimeRanges
    seekable: TimeRanges
    ended: bool
    autoplay: bool
    loop: bool
    def play(self) -> Awaitable[None]: ...
    def pause(self): ...
    controls: bool
    volume: float
    muted: bool
    defaultMuted: bool
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList
    def addTextTrack(self, kind: TextTrackKind, label: str | None = "", language: str | None = "") -> TextTrack: ...
    def captureStream(self) -> MediaStream: ...
    remote: RemotePlayback
    disableRemotePlayback: bool

class MediaDevices(EventTarget):
    def selectAudioOutput(self, options: AudioOutputOptions | None = {}) -> Awaitable[MediaDeviceInfo]: ...
    def setCaptureHandleConfig(self, config: CaptureHandleConfig | None = {}): ...
    def setSupportedCaptureActions(self, actions: Sequence[str]): ...
    oncaptureaction: EventHandler
    ondevicechange: EventHandler
    def enumerateDevices(self) -> Awaitable[Sequence[MediaDeviceInfo]]: ...
    def getSupportedConstraints(self) -> MediaTrackSupportedConstraints: ...
    def getUserMedia(self, constraints: MediaStreamConstraints | None = {}) -> Awaitable[MediaStream]: ...
    def getViewportMedia(self, constraints: ViewportMediaStreamConstraints | None = {}) -> Awaitable[MediaStream]: ...
    def getDisplayMedia(self, options: DisplayMediaStreamOptions | None = {}) -> Awaitable[MediaStream]: ...

class AudioOutputOptions(TypedDict):
    deviceId: NotRequired[str]

class Navigator(NavigatorBadge, NavigatorDeviceMemory, NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorContentUtils, NavigatorCookies, NavigatorPlugins, NavigatorConcurrentHardware, NavigatorNetworkInformation, NavigatorStorage, NavigatorUA, NavigatorLocks, NavigatorAutomationInformation, NavigatorGPU, NavigatorML):
    @overload
    def getAutoplayPolicy(self, type: AutoplayPolicyMediaType) -> AutoplayPolicy: ...
    @overload
    def getAutoplayPolicy(self, element: HTMLMediaElement) -> AutoplayPolicy: ...
    @overload
    def getAutoplayPolicy(self, context: AudioContext) -> AutoplayPolicy: ...
    def setClientBadge(self, contents: int | None = None) -> Awaitable[None]: ...
    def clearClientBadge(self) -> Awaitable[None]: ...
    def getBattery(self) -> Awaitable[BatteryManager]: ...
    def sendBeacon(self, url: USVString, data: BodyInit | None = None) -> bool: ...
    clipboard: Clipboard
    contacts: ContactsManager
    credentials: CredentialsContainer
    devicePosture: DevicePosture
    def requestMediaKeySystemAccess(self, keySystem: str, supportedConfigurations: Sequence[MediaKeySystemConfiguration]) -> Awaitable[MediaKeySystemAccess]: ...
    epubReadingSystem: EpubReadingSystem
    def getGamepads(self) -> Sequence[Gamepad | None]: ...
    geolocation: Geolocation
    def getInstalledRelatedApps(self) -> Awaitable[Sequence[RelatedApplication]]: ...
    userActivation: UserActivation
    ink: Ink
    scheduling: Scheduling
    keyboard: Keyboard
    mediaCapabilities: MediaCapabilities
    mediaDevices: MediaDevices
    def getUserMedia(self, constraints: MediaStreamConstraints, successCallback: NavigatorUserMediaSuccessCallback, errorCallback: NavigatorUserMediaErrorCallback): ...
    mediaSession: MediaSession
    permissions: Permissions
    maxTouchPoints: int
    presentation: Presentation
    wakeLock: WakeLock
    serial: Serial
    serviceWorker: ServiceWorkerContainer
    def vibrate(self, pattern: VibratePattern) -> bool: ...
    virtualKeyboard: VirtualKeyboard
    bluetooth: Bluetooth
    def share(self, data: ShareData | None = {}) -> Awaitable[None]: ...
    def canShare(self, data: ShareData | None = {}) -> bool: ...
    hid: HID
    def requestMIDIAccess(self, options: MIDIOptions | None = {}) -> Awaitable[MIDIAccess]: ...
    usb: USB
    xr: XRSystem
    windowControlsOverlay: WindowControlsOverlay

class ServiceWorkerGlobalScope(WorkerGlobalScope):
    onbackgroundfetchsuccess: EventHandler
    onbackgroundfetchfail: EventHandler
    onbackgroundfetchabort: EventHandler
    onbackgroundfetchclick: EventHandler
    onsync: EventHandler
    oncontentdelete: EventHandler
    cookieStore: CookieStore
    oncookiechange: EventHandler
    onnotificationclick: EventHandler
    onnotificationclose: EventHandler
    oncanmakepayment: EventHandler
    onpaymentrequest: EventHandler
    onperiodicsync: EventHandler
    onpush: EventHandler
    onpushsubscriptionchange: EventHandler
    clients: Clients
    registration: ServiceWorkerRegistration
    serviceWorker: ServiceWorker
    def skipWaiting(self) -> Awaitable[None]: ...
    oninstall: EventHandler
    onactivate: EventHandler
    onfetch: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler

class ServiceWorkerRegistration(EventTarget):
    backgroundFetch: BackgroundFetchManager
    sync: SyncManager
    index: ContentIndex
    cookies: CookieStoreManager
    def showNotification(self, title: str, options: NotificationOptions | None = {}) -> Awaitable[None]: ...
    def getNotifications(self, filter: GetNotificationOptions | None = {}) -> Awaitable[Sequence[Notification]]: ...
    paymentManager: PaymentManager
    periodicSync: PeriodicSyncManager
    pushManager: PushManager
    installing: ServiceWorker | None
    waiting: ServiceWorker | None
    active: ServiceWorker | None
    navigationPreload: NavigationPreloadManager
    scope: USVString
    updateViaCache: ServiceWorkerUpdateViaCache
    def update(self) -> Awaitable[None]: ...
    def unregister(self) -> Awaitable[bool]: ...
    onupdatefound: EventHandler

class BackgroundFetchManager:
    def fetch(self, id: str, requests: RequestInfo | Sequence[RequestInfo], options: BackgroundFetchOptions | None = {}) -> Awaitable[BackgroundFetchRegistration]: ...
    def get(self, id: str) -> Awaitable[BackgroundFetchRegistration | None]: ...
    def getIds(self) -> Awaitable[Sequence[str]]: ...

class BackgroundFetchUIOptions(TypedDict):
    icons: NotRequired[Sequence[ImageResource]]
    title: NotRequired[str]

class BackgroundFetchOptions(TypedDict, BackgroundFetchUIOptions):
    downloadTotal: NotRequired[int]

class BackgroundFetchRegistration(EventTarget):
    id: str
    uploadTotal: int
    uploaded: int
    downloadTotal: int
    downloaded: int
    result: BackgroundFetchResult
    failureReason: BackgroundFetchFailureReason
    recordsAvailable: bool
    onprogress: EventHandler
    def abort(self) -> Awaitable[bool]: ...
    def match(self, request: RequestInfo, options: CacheQueryOptions | None = {}) -> Awaitable[BackgroundFetchRecord]: ...
    def matchAll(self, request: RequestInfo | None = None, options: CacheQueryOptions | None = {}) -> Awaitable[Sequence[BackgroundFetchRecord]]: ...

class BackgroundFetchRecord:
    request: Request
    responseReady: Awaitable[Response]

class BackgroundFetchEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, init: BackgroundFetchEventInit) -> BackgroundFetchEvent: ...
    registration: BackgroundFetchRegistration

class BackgroundFetchEventInit(TypedDict, ExtendableEventInit):
    registration: BackgroundFetchRegistration

class BackgroundFetchUpdateUIEvent(BackgroundFetchEvent):
    @classmethod
    def new(self, type: str, init: BackgroundFetchEventInit) -> BackgroundFetchUpdateUIEvent: ...
    def updateUI(self, options: BackgroundFetchUIOptions | None = {}) -> Awaitable[None]: ...

class SyncManager:
    def register(self, tag: str) -> Awaitable[None]: ...
    def getTags(self) -> Awaitable[Sequence[str]]: ...

class SyncEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, init: SyncEventInit) -> SyncEvent: ...
    tag: str
    lastChance: bool

class SyncEventInit(TypedDict, ExtendableEventInit):
    tag: str
    lastChance: NotRequired[bool]

class NavigatorBadge:
    def setAppBadge(self, contents: int | None = None) -> Awaitable[None]: ...
    def clearAppBadge(self) -> Awaitable[None]: ...

class WorkerNavigator(NavigatorBadge, NavigatorDeviceMemory, NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorConcurrentHardware, NavigatorNetworkInformation, NavigatorStorage, NavigatorUA, NavigatorLocks, NavigatorGPU, NavigatorML):
    mediaCapabilities: MediaCapabilities
    permissions: Permissions
    serial: Serial
    serviceWorker: ServiceWorkerContainer
    hid: HID
    usb: USB

class BatteryManager(EventTarget):
    charging: bool
    chargingTime: float
    dischargingTime: float
    level: float
    onchargingchange: EventHandler
    onchargingtimechange: EventHandler
    ondischargingtimechange: EventHandler
    onlevelchange: EventHandler

class CaptureHandleConfig(TypedDict):
    exposeOrigin: NotRequired[bool]
    handle: NotRequired[str]
    permittedOrigins: NotRequired[Sequence[str]]

class CaptureHandle(TypedDict):
    origin: NotRequired[str]
    handle: NotRequired[str]

class MediaStreamTrack(EventTarget):
    def getCaptureHandle(self) -> CaptureHandle | None: ...
    oncapturehandlechange: EventHandler
    def getSupportedCaptureActions(self) -> Sequence[str]: ...
    def sendCaptureAction(self, action: CaptureAction) -> Awaitable[None]: ...
    kind: str
    id: str
    label: str
    enabled: bool
    muted: bool
    onmute: EventHandler
    onunmute: EventHandler
    readyState: MediaStreamTrackState
    onended: EventHandler
    def clone(self) -> MediaStreamTrack: ...
    def stop(self): ...
    def getCapabilities(self) -> MediaTrackCapabilities: ...
    def getConstraints(self) -> MediaTrackConstraints: ...
    def getSettings(self) -> MediaTrackSettings: ...
    def applyConstraints(self, constraints: MediaTrackConstraints | None = {}) -> Awaitable[None]: ...
    contentHint: str
    isolated: bool
    onisolationchange: EventHandler

class ClipboardEventInit(TypedDict, EventInit):
    clipboardData: NotRequired[DataTransfer | None]

class ClipboardEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: ClipboardEventInit | None = {}) -> ClipboardEvent: ...
    clipboardData: DataTransfer | None

class ClipboardItem:
    @classmethod
    def new(self, items: ClipboardItemData, options: ClipboardItemOptions | None = {}) -> ClipboardItem: ...
    presentationStyle: PresentationStyle
    types: Sequence[str]
    def getType(self, type: str) -> Awaitable[Blob]: ...

class ClipboardItemOptions(TypedDict):
    presentationStyle: NotRequired[PresentationStyle]

class Clipboard(EventTarget):
    def read(self) -> Awaitable[ClipboardItems]: ...
    def readText(self) -> Awaitable[str]: ...
    def write(self, data: ClipboardItems) -> Awaitable[None]: ...
    def writeText(self, data: str) -> Awaitable[None]: ...

class ClipboardPermissionDescriptor(TypedDict, PermissionDescriptor):
    allowWithoutGesture: NotRequired[bool]

class CloseWatcher(EventTarget):
    @classmethod
    def new(self, options: CloseWatcherOptions | None = {}) -> CloseWatcher: ...
    def destroy(self): ...
    def close(self): ...
    oncancel: EventHandler
    onclose: EventHandler

class CloseWatcherOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class Window(EventTarget, GlobalEventHandlers, WindowEventHandlers, WindowOrWorkerGlobalScope, AnimationFrameProvider, WindowSessionStorage, WindowLocalStorage):
    orientation: short
    onorientationchange: EventHandler
    cookieStore: CookieStore
    def navigate(self, dir: SpatialNavigationDirection): ...
    def matchMedia(self, query: CSSOMString) -> MediaQueryList: ...
    screen: Screen
    visualViewport: VisualViewport | None
    def moveTo(self, x: int, y: int): ...
    def moveBy(self, x: int, y: int): ...
    def resizeTo(self, width: int, height: int): ...
    def resizeBy(self, x: int, y: int): ...
    innerWidth: int
    innerHeight: int
    scrollX: float
    pageXOffset: float
    scrollY: float
    pageYOffset: float
    @overload
    def scroll(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scroll(self, x: float, y: float): ...
    @overload
    def scrollTo(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollTo(self, x: float, y: float): ...
    @overload
    def scrollBy(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollBy(self, x: float, y: float): ...
    screenX: int
    screenLeft: int
    screenY: int
    screenTop: int
    outerWidth: int
    outerHeight: int
    devicePixelRatio: float
    def getComputedStyle(self, elt: Element, pseudoElt: CSSOMString | None = None) -> CSSStyleDeclaration: ...
    def getDigitalGoodsService(self, serviceProvider: str) -> Awaitable[DigitalGoodsService]: ...
    event: Event | None
    def showOpenFilePicker(self, options: OpenFilePickerOptions | None = {}) -> Awaitable[Sequence[FileSystemFileHandle]]: ...
    def showSaveFilePicker(self, options: SaveFilePickerOptions | None = {}) -> Awaitable[FileSystemFileHandle]: ...
    def showDirectoryPicker(self, options: DirectoryPickerOptions | None = {}) -> Awaitable[FileSystemDirectoryHandle]: ...
    window: WindowProxy
    self: WindowProxy
    document: Document
    name: str
    location: Location
    history: History
    customElements: CustomElementRegistry
    locationbar: BarProp
    menubar: BarProp
    personalbar: BarProp
    scrollbars: BarProp
    statusbar: BarProp
    toolbar: BarProp
    status: str
    def close(self): ...
    closed: bool
    def stop(self): ...
    def focus(self): ...
    def blur(self): ...
    frames: WindowProxy
    length: int
    top: WindowProxy | None
    opener: Any
    parent: WindowProxy | None
    frameElement: Element | None
    def open(self, url: USVString | None = "", target: str | None = "_blank", features: str | None = "") -> WindowProxy | None: ...
    navigator: Navigator
    clientInformation: Navigator
    originAgentCluster: bool
    @overload
    def alert(self): ...
    @overload
    def alert(self, message: str): ...
    def confirm(self, message: str | None = "") -> bool: ...
    def prompt(self, message: str | None = "", default: str | None = "") -> str | None: ...
    def print(self): ...
    @overload
    def postMessage(self, message: Any, targetOrigin: USVString, transfer: Sequence[object] | None = []): ...
    @overload
    def postMessage(self, message: Any, options: WindowPostMessageOptions | None = {}): ...
    def captureEvents(self): ...
    def releaseEvents(self): ...
    external: External
    def queryLocalFonts(self, options: QueryOptions | None = {}) -> Awaitable[Sequence[FontData]]: ...
    onappinstalled: EventHandler
    onbeforeinstallprompt: EventHandler
    navigation: Navigation
    ondeviceorientation: EventHandler
    ondeviceorientationabsolute: EventHandler
    oncompassneedscalibration: EventHandler
    ondevicemotion: EventHandler
    portalHost: PortalHost | None
    def requestIdleCallback(self, callback: IdleRequestCallback, options: IdleRequestOptions | None = {}) -> int: ...
    def cancelIdleCallback(self, handle: int): ...
    def getSelection(self) -> Selection | None: ...
    speechSynthesis: SpeechSynthesis
    launchQueue: LaunchQueue
    def getScreenDetails(self) -> Awaitable[ScreenDetails]: ...

class HTMLBodyElement(HTMLElement, WindowEventHandlers):
    @classmethod
    def new(self) -> HTMLBodyElement: ...
    onorientationchange: EventHandler
    text: str
    link: str
    vLink: str
    aLink: str
    bgColor: str
    background: str

class CompressionStream(GenericTransformStream):
    @classmethod
    def new(self, format: str) -> CompressionStream: ...

class DecompressionStream(GenericTransformStream):
    @classmethod
    def new(self, format: str) -> DecompressionStream: ...

class PressureObserver:
    @classmethod
    def new(self, callback: PressureUpdateCallback, options: PressureObserverOptions | None = {}) -> PressureObserver: ...
    def observe(self, source: PressureSource) -> Awaitable[None]: ...
    def unobserve(self, source: PressureSource): ...
    def disconnect(self): ...
    def takeRecords(self) -> Sequence[PressureRecord]: ...

class PressureRecord:
    source: PressureSource
    state: PressureState
    factors: Sequence[PressureFactor]
    time: DOMHighResTimeStamp

class PressureObserverOptions(TypedDict):
    sampleRate: NotRequired[float]

class ConsoleNamespace:
    def assert_(self, condition: bool | None = false, *data: Any): ...
    def clear(self): ...
    def debug(self, *data: Any): ...
    def error(self, *data: Any): ...
    def info(self, *data: Any): ...
    def log(self, *data: Any): ...
    def table(self, tabularData: Any | None = None, properties: Sequence[str] | None = None): ...
    def trace(self, *data: Any): ...
    def warn(self, *data: Any): ...
    def dir(self, item: Any | None = None, options: object | None = None): ...
    def dirxml(self, *data: Any): ...
    def count(self, label: str | None = "default"): ...
    def countReset(self, label: str | None = "default"): ...
    def group(self, *data: Any): ...
    def groupCollapsed(self, *data: Any): ...
    def groupEnd(self): ...
    def time(self, label: str | None = "default"): ...
    def timeLog(self, label: str | None = "default", *data: Any): ...
    def timeEnd(self, label: str | None = "default"): ...

class ContactAddress:
    def toJSON(self) -> object: ...
    city: str
    country: str
    dependentLocality: str
    organization: str
    phone: str
    postalCode: str
    recipient: str
    region: str
    sortingCode: str
    addressLine: Sequence[str]

class ContactInfo(TypedDict):
    address: NotRequired[Sequence[ContactAddress]]
    email: NotRequired[Sequence[str]]
    icon: NotRequired[Sequence[Blob]]
    name: NotRequired[Sequence[str]]
    tel: NotRequired[Sequence[str]]

class ContactsSelectOptions(TypedDict):
    multiple: NotRequired[bool]

class ContactsManager:
    def getProperties(self) -> Awaitable[Sequence[ContactProperty]]: ...
    def select(self, properties: Sequence[ContactProperty], options: ContactsSelectOptions | None = {}) -> Awaitable[Sequence[ContactInfo]]: ...

class ContentDescription(TypedDict):
    id: str
    title: str
    description: str
    category: NotRequired[ContentCategory]
    icons: NotRequired[Sequence[ImageResource]]
    url: USVString

class ContentIndex:
    def add(self, description: ContentDescription) -> Awaitable[None]: ...
    def delete(self, id: str) -> Awaitable[None]: ...
    def getAll(self) -> Awaitable[Sequence[ContentDescription]]: ...

class ContentIndexEventInit(TypedDict, ExtendableEventInit):
    id: str

class ContentIndexEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, init: ContentIndexEventInit) -> ContentIndexEvent: ...
    id: str

class CookieStore(EventTarget):
    @overload
    def get(self, name: USVString) -> Awaitable[CookieListItem | None]: ...
    @overload
    def get(self, options: CookieStoreGetOptions | None = {}) -> Awaitable[CookieListItem | None]: ...
    @overload
    def getAll(self, name: USVString) -> Awaitable[CookieList]: ...
    @overload
    def getAll(self, options: CookieStoreGetOptions | None = {}) -> Awaitable[CookieList]: ...
    @overload
    def set(self, name: USVString, value: USVString) -> Awaitable[None]: ...
    @overload
    def set(self, options: CookieInit) -> Awaitable[None]: ...
    @overload
    def delete(self, name: USVString) -> Awaitable[None]: ...
    @overload
    def delete(self, options: CookieStoreDeleteOptions) -> Awaitable[None]: ...
    onchange: EventHandler

class CookieStoreGetOptions(TypedDict):
    name: NotRequired[USVString]
    url: NotRequired[USVString]

class CookieInit(TypedDict):
    name: USVString
    value: USVString
    expires: NotRequired[EpochTimeStamp | None]
    domain: NotRequired[USVString | None]
    path: NotRequired[USVString]
    sameSite: NotRequired[CookieSameSite]

class CookieStoreDeleteOptions(TypedDict):
    name: USVString
    domain: NotRequired[USVString | None]
    path: NotRequired[USVString]

class CookieListItem(TypedDict):
    name: NotRequired[USVString]
    value: NotRequired[USVString]
    domain: NotRequired[USVString | None]
    path: NotRequired[USVString]
    expires: NotRequired[EpochTimeStamp | None]
    secure: NotRequired[bool]
    sameSite: NotRequired[CookieSameSite]

class CookieStoreManager:
    def subscribe(self, subscriptions: Sequence[CookieStoreGetOptions]) -> Awaitable[None]: ...
    def getSubscriptions(self) -> Awaitable[Sequence[CookieStoreGetOptions]]: ...
    def unsubscribe(self, subscriptions: Sequence[CookieStoreGetOptions]) -> Awaitable[None]: ...

class CookieChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: CookieChangeEventInit | None = {}) -> CookieChangeEvent: ...
    changed: Sequence[CookieListItem]
    deleted: Sequence[CookieListItem]

class CookieChangeEventInit(TypedDict, EventInit):
    changed: NotRequired[CookieList]
    deleted: NotRequired[CookieList]

class ExtendableCookieChangeEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: ExtendableCookieChangeEventInit | None = {}) -> ExtendableCookieChangeEvent: ...
    changed: Sequence[CookieListItem]
    deleted: Sequence[CookieListItem]

class ExtendableCookieChangeEventInit(TypedDict, ExtendableEventInit):
    changed: NotRequired[CookieList]
    deleted: NotRequired[CookieList]

class CrashReportBody(ReportBody):
    def toJSON(self) -> object: ...
    reason: str | None

class Credential:
    id: USVString
    type: str

class CredentialUserData:
    name: USVString
    iconURL: USVString

class CredentialsContainer:
    def get(self, options: CredentialRequestOptions | None = {}) -> Awaitable[Credential | None]: ...
    def store(self, credential: Credential) -> Awaitable[Credential]: ...
    def create(self, options: CredentialCreationOptions | None = {}) -> Awaitable[Credential | None]: ...
    def preventSilentAccess(self) -> Awaitable[None]: ...

class CredentialData(TypedDict):
    id: USVString

class CredentialCreationOptions(TypedDict, TypedDict, TypedDict, TypedDict):
    signal: NotRequired[AbortSignal]
    password: NotRequired[PasswordCredentialInit]
    federated: NotRequired[FederatedCredentialInit]
    publicKey: NotRequired[PublicKeyCredentialCreationOptions]

class PasswordCredential(Credential, CredentialUserData):
    @overload
    @classmethod
    def new(self, form: HTMLFormElement) -> PasswordCredential: ...
    @overload
    @classmethod
    def new(self, data: PasswordCredentialData) -> PasswordCredential: ...
    password: USVString

class PasswordCredentialData(TypedDict, CredentialData):
    name: NotRequired[USVString]
    iconURL: NotRequired[USVString]
    origin: USVString
    password: USVString

class FederatedCredential(Credential, CredentialUserData):
    @classmethod
    def new(self, data: FederatedCredentialInit) -> FederatedCredential: ...
    provider: USVString
    protocol: str | None

class FederatedCredentialRequestOptions(TypedDict):
    providers: NotRequired[Sequence[USVString]]
    protocols: NotRequired[Sequence[str]]

class FederatedCredentialInit(TypedDict, CredentialData):
    name: NotRequired[USVString]
    iconURL: NotRequired[USVString]
    origin: USVString
    provider: USVString
    protocol: NotRequired[str]

class HTMLIFrameElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLIFrameElement: ...
    csp: str
    src: USVString
    srcdoc: str
    name: str
    sandbox: DOMTokenList
    allow: str
    allowFullscreen: bool
    width: str
    height: str
    referrerPolicy: str
    loading: str
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    def getSVGDocument(self) -> Document | None: ...
    align: str
    scrolling: str
    frameBorder: str
    longDesc: USVString
    marginHeight: str
    marginWidth: str
    permissionsPolicy: PermissionsPolicy
    fetchPriority: str

class ScriptingPolicyReportBody(ReportBody):
    def toJSON(self) -> object: ...
    violationType: str
    violationURL: USVString | None
    violationSample: USVString | None
    lineno: int
    colno: int

class AnimationWorkletGlobalScope(WorkletGlobalScope):
    def registerAnimator(self, name: str, animatorCtor: AnimatorInstanceConstructor): ...

class WorkletAnimationEffect:
    def getTiming(self) -> EffectTiming: ...
    def getComputedTiming(self) -> ComputedEffectTiming: ...
    localTime: float | None

class WorkletAnimation(Animation):
    @classmethod
    def new(self, animatorName: str, effects: AnimationEffect | Sequence[AnimationEffect] | None = None, timeline: AnimationTimeline | None = None, options: Any | None = None) -> WorkletAnimation: ...
    animatorName: str

class WorkletGroupEffect:
    def getChildren(self) -> Sequence[WorkletAnimationEffect]: ...

class CSSAnimation(Animation):
    animationName: CSSOMString

class AnimationEvent(Event):
    @classmethod
    def new(self, type: CSSOMString, animationEventInitDict: AnimationEventInit | None = {}) -> AnimationEvent: ...
    animationName: CSSOMString
    elapsedTime: float
    pseudoElement: CSSOMString

class AnimationEventInit(TypedDict, EventInit):
    animationName: NotRequired[CSSOMString]
    elapsedTime: NotRequired[float]
    pseudoElement: NotRequired[CSSOMString]

class CSSRule:
    KEYFRAMES_RULE = 7
    KEYFRAME_RULE = 8
    SUPPORTS_RULE = 12
    COUNTER_STYLE_RULE = 11
    FONT_FEATURE_VALUES_RULE = 14
    cssText: CSSOMString
    parentRule: CSSRule | None
    parentStyleSheet: CSSStyleSheet | None
    type: int
    STYLE_RULE = 1
    CHARSET_RULE = 2
    IMPORT_RULE = 3
    MEDIA_RULE = 4
    FONT_FACE_RULE = 5
    PAGE_RULE = 6
    MARGIN_RULE = 9
    NAMESPACE_RULE = 10

class CSSKeyframeRule(CSSRule):
    keyText: CSSOMString
    style: CSSStyleDeclaration

class CSSKeyframesRule(CSSRule):
    name: CSSOMString
    cssRules: CSSRuleList
    length: int
    def appendRule(self, rule: CSSOMString): ...
    def deleteRule(self, select: CSSOMString): ...
    def findRule(self, select: CSSOMString) -> CSSKeyframeRule | None: ...

class GlobalEventHandlers:
    onanimationstart: EventHandler
    onanimationiteration: EventHandler
    onanimationend: EventHandler
    onanimationcancel: EventHandler
    ontransitionrun: EventHandler
    ontransitionstart: EventHandler
    ontransitionend: EventHandler
    ontransitioncancel: EventHandler
    onabort: EventHandler
    onauxclick: EventHandler
    onbeforeinput: EventHandler
    onbeforematch: EventHandler
    onblur: EventHandler
    oncancel: EventHandler
    oncanplay: EventHandler
    oncanplaythrough: EventHandler
    onchange: EventHandler
    onclick: EventHandler
    onclose: EventHandler
    oncontextlost: EventHandler
    oncontextmenu: EventHandler
    oncontextrestored: EventHandler
    oncopy: EventHandler
    oncuechange: EventHandler
    oncut: EventHandler
    ondblclick: EventHandler
    ondrag: EventHandler
    ondragend: EventHandler
    ondragenter: EventHandler
    ondragleave: EventHandler
    ondragover: EventHandler
    ondragstart: EventHandler
    ondrop: EventHandler
    ondurationchange: EventHandler
    onemptied: EventHandler
    onended: EventHandler
    onerror: OnErrorEventHandler
    onfocus: EventHandler
    onformdata: EventHandler
    oninput: EventHandler
    oninvalid: EventHandler
    onkeydown: EventHandler
    onkeypress: EventHandler
    onkeyup: EventHandler
    onload: EventHandler
    onloadeddata: EventHandler
    onloadedmetadata: EventHandler
    onloadstart: EventHandler
    onmousedown: EventHandler
    onmouseenter: EventHandler
    onmouseleave: EventHandler
    onmousemove: EventHandler
    onmouseout: EventHandler
    onmouseover: EventHandler
    onmouseup: EventHandler
    onpaste: EventHandler
    onpause: EventHandler
    onplay: EventHandler
    onplaying: EventHandler
    onprogress: EventHandler
    onratechange: EventHandler
    onreset: EventHandler
    onresize: EventHandler
    onscroll: EventHandler
    onscrollend: EventHandler
    onsecuritypolicyviolation: EventHandler
    onseeked: EventHandler
    onseeking: EventHandler
    onselect: EventHandler
    onslotchange: EventHandler
    onstalled: EventHandler
    onsubmit: EventHandler
    onsuspend: EventHandler
    ontimeupdate: EventHandler
    ontoggle: EventHandler
    onvolumechange: EventHandler
    onwaiting: EventHandler
    onwebkitanimationend: EventHandler
    onwebkitanimationiteration: EventHandler
    onwebkitanimationstart: EventHandler
    onwebkittransitionend: EventHandler
    onwheel: EventHandler
    onpointerover: EventHandler
    onpointerenter: EventHandler
    onpointerdown: EventHandler
    onpointermove: EventHandler
    onpointerrawupdate: EventHandler
    onpointerup: EventHandler
    onpointercancel: EventHandler
    onpointerout: EventHandler
    onpointerleave: EventHandler
    ongotpointercapture: EventHandler
    onlostpointercapture: EventHandler
    onselectstart: EventHandler
    onselectionchange: EventHandler
    ontouchstart: EventHandler
    ontouchend: EventHandler
    ontouchmove: EventHandler
    ontouchcancel: EventHandler
    onbeforexrselect: EventHandler

class CSSImportRule(CSSRule):
    layerName: CSSOMString | None
    href: USVString
    media: MediaList
    styleSheet: CSSStyleSheet

class CSSLayerBlockRule(CSSGroupingRule):
    name: CSSOMString

class CSSLayerStatementRule(CSSRule):
    nameList: Sequence[CSSOMString]

class CSSColorProfileRule(CSSRule):
    name: CSSOMString
    src: CSSOMString
    renderingIntent: CSSOMString
    components: CSSOMString

class CSSConditionRule(CSSGroupingRule):
    conditionText: CSSOMString

class CSSMediaRule(CSSConditionRule):
    media: MediaList

class CSSSupportsRule(CSSConditionRule): ...

class CssNamespace:
    @overload
    def supports(self, property: CSSOMString, value: CSSOMString) -> bool: ...
    @overload
    def supports(self, conditionText: CSSOMString) -> bool: ...
    def parseStylesheet(self, css: CSSStringSource, options: CSSParserOptions | None = {}) -> Awaitable[Sequence[CSSParserRule]]: ...
    def parseRuleList(self, css: CSSStringSource, options: CSSParserOptions | None = {}) -> Awaitable[Sequence[CSSParserRule]]: ...
    def parseRule(self, css: CSSStringSource, options: CSSParserOptions | None = {}) -> Awaitable[CSSParserRule]: ...
    def parseDeclarationList(self, css: CSSStringSource, options: CSSParserOptions | None = {}) -> Awaitable[Sequence[CSSParserRule]]: ...
    def parseDeclaration(self, css: str, options: CSSParserOptions | None = {}) -> CSSParserDeclaration: ...
    def parseValue(self, css: str) -> CSSToken: ...
    def parseValueList(self, css: str) -> Sequence[CSSToken]: ...
    def parseCommaValueList(self, css: str) -> Sequence[Sequence[CSSToken]]: ...
    def registerProperty(self, definition: PropertyDefinition): ...
    def number(self, value: float) -> CSSUnitValue: ...
    def percent(self, value: float) -> CSSUnitValue: ...
    def em(self, value: float) -> CSSUnitValue: ...
    def ex(self, value: float) -> CSSUnitValue: ...
    def ch(self, value: float) -> CSSUnitValue: ...
    def ic(self, value: float) -> CSSUnitValue: ...
    def rem(self, value: float) -> CSSUnitValue: ...
    def lh(self, value: float) -> CSSUnitValue: ...
    def rlh(self, value: float) -> CSSUnitValue: ...
    def vw(self, value: float) -> CSSUnitValue: ...
    def vh(self, value: float) -> CSSUnitValue: ...
    def vi(self, value: float) -> CSSUnitValue: ...
    def vb(self, value: float) -> CSSUnitValue: ...
    def vmin(self, value: float) -> CSSUnitValue: ...
    def vmax(self, value: float) -> CSSUnitValue: ...
    def svw(self, value: float) -> CSSUnitValue: ...
    def svh(self, value: float) -> CSSUnitValue: ...
    def svi(self, value: float) -> CSSUnitValue: ...
    def svb(self, value: float) -> CSSUnitValue: ...
    def svmin(self, value: float) -> CSSUnitValue: ...
    def svmax(self, value: float) -> CSSUnitValue: ...
    def lvw(self, value: float) -> CSSUnitValue: ...
    def lvh(self, value: float) -> CSSUnitValue: ...
    def lvi(self, value: float) -> CSSUnitValue: ...
    def lvb(self, value: float) -> CSSUnitValue: ...
    def lvmin(self, value: float) -> CSSUnitValue: ...
    def lvmax(self, value: float) -> CSSUnitValue: ...
    def dvw(self, value: float) -> CSSUnitValue: ...
    def dvh(self, value: float) -> CSSUnitValue: ...
    def dvi(self, value: float) -> CSSUnitValue: ...
    def dvb(self, value: float) -> CSSUnitValue: ...
    def dvmin(self, value: float) -> CSSUnitValue: ...
    def dvmax(self, value: float) -> CSSUnitValue: ...
    def cqw(self, value: float) -> CSSUnitValue: ...
    def cqh(self, value: float) -> CSSUnitValue: ...
    def cqi(self, value: float) -> CSSUnitValue: ...
    def cqb(self, value: float) -> CSSUnitValue: ...
    def cqmin(self, value: float) -> CSSUnitValue: ...
    def cqmax(self, value: float) -> CSSUnitValue: ...
    def cm(self, value: float) -> CSSUnitValue: ...
    def mm(self, value: float) -> CSSUnitValue: ...
    def Q(self, value: float) -> CSSUnitValue: ...
    def in_(self, value: float) -> CSSUnitValue: ...
    def pt(self, value: float) -> CSSUnitValue: ...
    def pc(self, value: float) -> CSSUnitValue: ...
    def px(self, value: float) -> CSSUnitValue: ...
    def deg(self, value: float) -> CSSUnitValue: ...
    def grad(self, value: float) -> CSSUnitValue: ...
    def rad(self, value: float) -> CSSUnitValue: ...
    def turn(self, value: float) -> CSSUnitValue: ...
    def s(self, value: float) -> CSSUnitValue: ...
    def ms(self, value: float) -> CSSUnitValue: ...
    def Hz(self, value: float) -> CSSUnitValue: ...
    def kHz(self, value: float) -> CSSUnitValue: ...
    def dpi(self, value: float) -> CSSUnitValue: ...
    def dpcm(self, value: float) -> CSSUnitValue: ...
    def dppx(self, value: float) -> CSSUnitValue: ...
    def fr(self, value: float) -> CSSUnitValue: ...
    def escape(self, ident: CSSOMString) -> CSSOMString: ...

class CSSContainerRule(CSSConditionRule):
    containerName: CSSOMString
    containerQuery: CSSOMString

class ContentVisibilityAutoStateChangedEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: ContentVisibilityAutoStateChangedEventInit | None = {}) -> ContentVisibilityAutoStateChangedEvent: ...
    skipped: bool

class ContentVisibilityAutoStateChangedEventInit(TypedDict, EventInit):
    skipped: NotRequired[bool]

class CSSCounterStyleRule(CSSRule):
    name: CSSOMString
    system: CSSOMString
    symbols: CSSOMString
    additiveSymbols: CSSOMString
    negative: CSSOMString
    prefix: CSSOMString
    suffix: CSSOMString
    range: CSSOMString
    pad: CSSOMString
    speakAs: CSSOMString
    fallback: CSSOMString

class FontFaceDescriptors(TypedDict):
    style: NotRequired[CSSOMString]
    weight: NotRequired[CSSOMString]
    stretch: NotRequired[CSSOMString]
    unicodeRange: NotRequired[CSSOMString]
    variant: NotRequired[CSSOMString]
    featureSettings: NotRequired[CSSOMString]
    variationSettings: NotRequired[CSSOMString]
    display: NotRequired[CSSOMString]
    ascentOverride: NotRequired[CSSOMString]
    descentOverride: NotRequired[CSSOMString]
    lineGapOverride: NotRequired[CSSOMString]

class FontFace:
    @classmethod
    def new(self, family: CSSOMString, source: CSSOMString | BinaryData, descriptors: FontFaceDescriptors | None = {}) -> FontFace: ...
    family: CSSOMString
    style: CSSOMString
    weight: CSSOMString
    stretch: CSSOMString
    unicodeRange: CSSOMString
    variant: CSSOMString
    featureSettings: CSSOMString
    variationSettings: CSSOMString
    display: CSSOMString
    ascentOverride: CSSOMString
    descentOverride: CSSOMString
    lineGapOverride: CSSOMString
    status: FontFaceLoadStatus
    def load(self) -> Awaitable[FontFace]: ...
    loaded: Awaitable[FontFace]
    features: FontFaceFeatures
    variations: FontFaceVariations
    palettes: FontFacePalettes

class FontFaceFeatures: ...

class FontFaceVariationAxis:
    name: str
    axisTag: str
    minimumValue: float
    maximumValue: float
    defaultValue: float

class FontFaceVariations: ...

class FontFacePalette:
    length: int
    usableWithLightBackground: bool
    usableWithDarkBackground: bool

class FontFacePalettes:
    length: int

class FontFaceSetLoadEventInit(TypedDict, EventInit):
    fontfaces: NotRequired[Sequence[FontFace]]

class FontFaceSetLoadEvent(Event):
    @classmethod
    def new(self, type: CSSOMString, eventInitDict: FontFaceSetLoadEventInit | None = {}) -> FontFaceSetLoadEvent: ...
    fontfaces: Sequence[FontFace]

class FontFaceSet(EventTarget):
    @classmethod
    def new(self, initialFaces: Sequence[FontFace]) -> FontFaceSet: ...
    def add(self, font: FontFace) -> FontFaceSet: ...
    def delete(self, font: FontFace) -> bool: ...
    def clear(self): ...
    onloading: EventHandler
    onloadingdone: EventHandler
    onloadingerror: EventHandler
    def load(self, font: CSSOMString, text: CSSOMString | None = " ") -> Awaitable[Sequence[FontFace]]: ...
    def check(self, font: CSSOMString, text: CSSOMString | None = " ") -> bool: ...
    ready: Awaitable[FontFaceSet]
    status: FontFaceSetLoadStatus

class FontFaceSource:
    fonts: FontFaceSet

class WorkerGlobalScope(EventTarget, FontFaceSource, WindowOrWorkerGlobalScope):
    self: WorkerGlobalScope
    location: WorkerLocation
    navigator: WorkerNavigator
    def importScripts(self, *urls: USVString): ...
    onerror: OnErrorEventHandler
    onlanguagechange: EventHandler
    onoffline: EventHandler
    ononline: EventHandler
    onrejectionhandled: EventHandler
    onunhandledrejection: EventHandler

class CSSFontFaceRule(CSSRule):
    style: CSSStyleDeclaration

class CSSFontFeatureValuesRule(CSSRule):
    fontFamily: CSSOMString
    annotation: CSSFontFeatureValuesMap
    ornaments: CSSFontFeatureValuesMap
    stylistic: CSSFontFeatureValuesMap
    swash: CSSFontFeatureValuesMap
    characterVariant: CSSFontFeatureValuesMap
    styleset: CSSFontFeatureValuesMap

class CSSFontFeatureValuesMap:
    def set(self, featureValueName: CSSOMString, values: int | Sequence[int]): ...

class CSSFontPaletteValuesRule(CSSRule):
    name: CSSOMString
    fontFamily: CSSOMString
    basePalette: CSSOMString
    overrideColors: CSSOMString

class Highlight:
    @classmethod
    def new(self, *initialRanges: AbstractRange) -> Highlight: ...
    priority: int
    type: HighlightType

class HighlightRegistry: ...

class LayoutWorkletGlobalScope(WorkletGlobalScope):
    def registerLayout(self, name: str, layoutCtor: VoidFunction): ...

class LayoutOptions(TypedDict):
    childDisplay: NotRequired[ChildDisplayType]
    sizing: NotRequired[LayoutSizingMode]

class LayoutChild:
    styleMap: StylePropertyMapReadOnly
    def intrinsicSizes(self) -> Awaitable[IntrinsicSizes]: ...
    def layoutNextFragment(self, constraints: LayoutConstraintsOptions, breakToken: ChildBreakToken) -> Awaitable[LayoutFragment]: ...

class LayoutFragment:
    inlineSize: float
    blockSize: float
    inlineOffset: float
    blockOffset: float
    data: Any
    breakToken: ChildBreakToken | None

class IntrinsicSizes:
    minContentSize: float
    maxContentSize: float

class LayoutConstraints:
    availableInlineSize: float
    availableBlockSize: float
    fixedInlineSize: float | None
    fixedBlockSize: float | None
    percentageInlineSize: float
    percentageBlockSize: float
    blockFragmentationOffset: float | None
    blockFragmentationType: BlockFragmentationType
    data: Any

class LayoutConstraintsOptions(TypedDict):
    availableInlineSize: NotRequired[float]
    availableBlockSize: NotRequired[float]
    fixedInlineSize: NotRequired[float]
    fixedBlockSize: NotRequired[float]
    percentageInlineSize: NotRequired[float]
    percentageBlockSize: NotRequired[float]
    blockFragmentationOffset: NotRequired[float]
    blockFragmentationType: NotRequired[BlockFragmentationType]
    data: NotRequired[Any]

class ChildBreakToken:
    breakType: BreakType
    child: LayoutChild

class BreakToken:
    childBreakTokens: Sequence[ChildBreakToken]
    data: Any

class BreakTokenOptions(TypedDict):
    childBreakTokens: NotRequired[Sequence[ChildBreakToken]]
    data: NotRequired[Any]

class LayoutEdges:
    inlineStart: float
    inlineEnd: float
    blockStart: float
    blockEnd: float
    inline: float
    block: float

class FragmentResultOptions(TypedDict):
    inlineSize: NotRequired[float]
    blockSize: NotRequired[float]
    autoBlockSize: NotRequired[float]
    childFragments: NotRequired[Sequence[LayoutFragment]]
    data: NotRequired[Any]
    breakToken: NotRequired[BreakTokenOptions]

class FragmentResult:
    @classmethod
    def new(self, options: FragmentResultOptions | None = {}) -> FragmentResult: ...
    inlineSize: float
    blockSize: float

class IntrinsicSizesResultOptions(TypedDict):
    maxContentSize: NotRequired[float]
    minContentSize: NotRequired[float]

class SVGClipPathElement(SVGElement):
    clipPathUnits: SVGAnimatedEnumeration
    transform: SVGAnimatedTransformList

class SVGMaskElement(SVGElement):
    maskUnits: SVGAnimatedEnumeration
    maskContentUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class FocusableAreasOption(TypedDict):
    mode: NotRequired[FocusableAreaSearchMode]

class SpatialNavigationSearchOptions(TypedDict):
    candidates: NotRequired[Sequence[Node]]
    container: NotRequired[Node | None]

class NavigationEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: NavigationEventInit | None = {}) -> NavigationEvent: ...
    dir: SpatialNavigationDirection
    relatedTarget: EventTarget | None

class NavigationEventInit(TypedDict, UIEventInit):
    dir: NotRequired[SpatialNavigationDirection]
    relatedTarget: NotRequired[EventTarget | None]

class CSSStyleRule(CSSRule):
    cssRules: CSSRuleList
    def insertRule(self, rule: CSSOMString, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...
    styleMap: StylePropertyMap
    selectorText: CSSOMString
    style: CSSStyleDeclaration

class PaintWorkletGlobalScope(WorkletGlobalScope):
    def registerPaint(self, name: str, paintCtor: VoidFunction): ...
    devicePixelRatio: float

class PaintRenderingContext2DSettings(TypedDict):
    alpha: NotRequired[bool]

class PaintRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasRect, CanvasDrawPath, CanvasDrawImage, CanvasPathDrawingStyles, CanvasPath): ...

class PaintSize:
    width: float
    height: float

class CSSParserOptions(TypedDict):
    atRules: NotRequired[object]

class CSSParserRule: ...

class CSSParserAtRule(CSSParserRule):
    @classmethod
    def new(self, name: str, prelude: Sequence[CSSToken], body: Sequence[CSSParserRule] | None = None) -> CSSParserAtRule: ...
    name: str
    prelude: Sequence[CSSParserValue]
    body: Sequence[CSSParserRule]

class CSSParserQualifiedRule(CSSParserRule):
    @classmethod
    def new(self, prelude: Sequence[CSSToken], body: Sequence[CSSParserRule] | None = None) -> CSSParserQualifiedRule: ...
    prelude: Sequence[CSSParserValue]
    body: Sequence[CSSParserRule]

class CSSParserDeclaration(CSSParserRule):
    @classmethod
    def new(self, name: str, body: Sequence[CSSParserRule] | None = None) -> CSSParserDeclaration: ...
    name: str
    body: Sequence[CSSParserValue]

class CSSParserValue: ...

class CSSParserBlock(CSSParserValue):
    @classmethod
    def new(self, name: str, body: Sequence[CSSParserValue]) -> CSSParserBlock: ...
    name: str
    body: Sequence[CSSParserValue]

class CSSParserFunction(CSSParserValue):
    @classmethod
    def new(self, name: str, args: Sequence[Sequence[CSSParserValue]]) -> CSSParserFunction: ...
    name: str
    args: Sequence[Sequence[CSSParserValue]]

class PropertyDefinition(TypedDict):
    name: str
    syntax: NotRequired[str]
    inherits: bool
    initialValue: NotRequired[str]

class CSSPropertyRule(CSSRule):
    name: CSSOMString
    syntax: CSSOMString
    inherits: bool
    initialValue: CSSOMString | None

class CSSPseudoElement(EventTarget, GeometryUtils):
    type: CSSOMString
    element: Element
    parent: Element | CSSPseudoElement
    def pseudo(self, type: CSSOMString) -> CSSPseudoElement | None: ...

class NamedFlowMap: ...

class NamedFlow(EventTarget):
    name: CSSOMString
    overset: bool
    def getRegions(self) -> Sequence[Element]: ...
    firstEmptyRegionIndex: short
    def getContent(self) -> Sequence[Node]: ...
    def getRegionsByContent(self, node: Node) -> Sequence[Element]: ...

class Region:
    regionOverset: CSSOMString
    def getRegionFlowRanges(self) -> Sequence[Range]: ...

class CSSTransition(Animation):
    transitionProperty: CSSOMString

class TransitionEvent(Event):
    @classmethod
    def new(self, type: CSSOMString, transitionEventInitDict: TransitionEventInit | None = {}) -> TransitionEvent: ...
    propertyName: CSSOMString
    elapsedTime: float
    pseudoElement: CSSOMString

class TransitionEventInit(TypedDict, EventInit):
    propertyName: NotRequired[CSSOMString]
    elapsedTime: NotRequired[float]
    pseudoElement: NotRequired[CSSOMString]

class CSSStyleValue: ...

class StylePropertyMapReadOnly:
    def get(self, property: USVString) -> Any: ...
    def getAll(self, property: USVString) -> Sequence[CSSStyleValue]: ...
    def has(self, property: USVString) -> bool: ...
    size: int

class StylePropertyMap(StylePropertyMapReadOnly):
    def set(self, property: USVString, *values: CSSStyleValue | USVString): ...
    def append(self, property: USVString, *values: CSSStyleValue | USVString): ...
    def delete(self, property: USVString): ...
    def clear(self): ...

class ElementCSSInlineStyle:
    attributeStyleMap: StylePropertyMap
    style: CSSStyleDeclaration

class CSSUnparsedValue(CSSStyleValue):
    @classmethod
    def new(self, members: Sequence[CSSUnparsedSegment]) -> CSSUnparsedValue: ...
    length: int

class CSSVariableReferenceValue:
    @classmethod
    def new(self, variable: USVString, fallback: CSSUnparsedValue | None = None) -> CSSVariableReferenceValue: ...
    variable: USVString
    fallback: CSSUnparsedValue | None

class CSSKeywordValue(CSSStyleValue):
    @classmethod
    def new(self, value: USVString) -> CSSKeywordValue: ...
    value: USVString

class CSSNumericType(TypedDict):
    length: NotRequired[int]
    angle: NotRequired[int]
    time: NotRequired[int]
    frequency: NotRequired[int]
    resolution: NotRequired[int]
    flex: NotRequired[int]
    percent: NotRequired[int]
    percentHint: NotRequired[CSSNumericBaseType]

class CSSNumericValue(CSSStyleValue):
    def add(self, *values: CSSNumberish) -> CSSNumericValue: ...
    def sub(self, *values: CSSNumberish) -> CSSNumericValue: ...
    def mul(self, *values: CSSNumberish) -> CSSNumericValue: ...
    def div(self, *values: CSSNumberish) -> CSSNumericValue: ...
    def min(self, *values: CSSNumberish) -> CSSNumericValue: ...
    def max(self, *values: CSSNumberish) -> CSSNumericValue: ...
    def equals(self, *value: CSSNumberish) -> bool: ...
    def to(self, unit: USVString) -> CSSUnitValue: ...
    def toSum(self, *units: USVString) -> CSSMathSum: ...
    def type(self) -> CSSNumericType: ...

class CSSUnitValue(CSSNumericValue):
    @classmethod
    def new(self, value: float, unit: USVString) -> CSSUnitValue: ...
    value: float
    unit: USVString

class CSSMathValue(CSSNumericValue):
    operator: CSSMathOperator

class CSSMathSum(CSSMathValue):
    @classmethod
    def new(self, *args: CSSNumberish) -> CSSMathSum: ...
    values: CSSNumericArray

class CSSMathProduct(CSSMathValue):
    @classmethod
    def new(self, *args: CSSNumberish) -> CSSMathProduct: ...
    values: CSSNumericArray

class CSSMathNegate(CSSMathValue):
    @classmethod
    def new(self, arg: CSSNumberish) -> CSSMathNegate: ...
    value: CSSNumericValue

class CSSMathInvert(CSSMathValue):
    @classmethod
    def new(self, arg: CSSNumberish) -> CSSMathInvert: ...
    value: CSSNumericValue

class CSSMathMin(CSSMathValue):
    @classmethod
    def new(self, *args: CSSNumberish) -> CSSMathMin: ...
    values: CSSNumericArray

class CSSMathMax(CSSMathValue):
    @classmethod
    def new(self, *args: CSSNumberish) -> CSSMathMax: ...
    values: CSSNumericArray

class CSSMathClamp(CSSMathValue):
    @classmethod
    def new(self, lower: CSSNumberish, value: CSSNumberish, upper: CSSNumberish) -> CSSMathClamp: ...
    lower: CSSNumericValue
    value: CSSNumericValue
    upper: CSSNumericValue

class CSSNumericArray:
    length: int

class CSSTransformValue(CSSStyleValue):
    @classmethod
    def new(self, transforms: Sequence[CSSTransformComponent]) -> CSSTransformValue: ...
    length: int
    is2D: bool
    def toMatrix(self) -> DOMMatrix: ...

class CSSTransformComponent:
    is2D: bool
    def toMatrix(self) -> DOMMatrix: ...

class CSSTranslate(CSSTransformComponent):
    @classmethod
    def new(self, x: CSSNumericValue, y: CSSNumericValue, z: CSSNumericValue | None = None) -> CSSTranslate: ...
    x: CSSNumericValue
    y: CSSNumericValue
    z: CSSNumericValue

class CSSRotate(CSSTransformComponent):
    @overload
    @classmethod
    def new(self, angle: CSSNumericValue) -> CSSRotate: ...
    @overload
    @classmethod
    def new(self, x: CSSNumberish, y: CSSNumberish, z: CSSNumberish, angle: CSSNumericValue) -> CSSRotate: ...
    x: CSSNumberish
    y: CSSNumberish
    z: CSSNumberish
    angle: CSSNumericValue

class CSSScale(CSSTransformComponent):
    @classmethod
    def new(self, x: CSSNumberish, y: CSSNumberish, z: CSSNumberish | None = None) -> CSSScale: ...
    x: CSSNumberish
    y: CSSNumberish
    z: CSSNumberish

class CSSSkew(CSSTransformComponent):
    @classmethod
    def new(self, ax: CSSNumericValue, ay: CSSNumericValue) -> CSSSkew: ...
    ax: CSSNumericValue
    ay: CSSNumericValue

class CSSSkewX(CSSTransformComponent):
    @classmethod
    def new(self, ax: CSSNumericValue) -> CSSSkewX: ...
    ax: CSSNumericValue

class CSSSkewY(CSSTransformComponent):
    @classmethod
    def new(self, ay: CSSNumericValue) -> CSSSkewY: ...
    ay: CSSNumericValue

class CSSPerspective(CSSTransformComponent):
    @classmethod
    def new(self, length: CSSPerspectiveValue) -> CSSPerspective: ...
    length: CSSPerspectiveValue

class CSSMatrixComponent(CSSTransformComponent):
    @classmethod
    def new(self, matrix: DOMMatrixReadOnly, options: CSSMatrixComponentOptions | None = {}) -> CSSMatrixComponent: ...
    matrix: DOMMatrix

class CSSMatrixComponentOptions(TypedDict):
    is2D: NotRequired[bool]

class CSSImageValue(CSSStyleValue): ...

class CSSColorValue(CSSStyleValue): ...

class CSSRGB(CSSColorValue):
    @classmethod
    def new(self, r: CSSColorRGBComp, g: CSSColorRGBComp, b: CSSColorRGBComp, alpha: CSSColorPercent | None = 1) -> CSSRGB: ...
    r: CSSColorRGBComp
    g: CSSColorRGBComp
    b: CSSColorRGBComp
    alpha: CSSColorPercent

class CSSHSL(CSSColorValue):
    @classmethod
    def new(self, h: CSSColorAngle, s: CSSColorPercent, l: CSSColorPercent, alpha: CSSColorPercent | None = 1) -> CSSHSL: ...
    h: CSSColorAngle
    s: CSSColorPercent
    l: CSSColorPercent
    alpha: CSSColorPercent

class CSSHWB(CSSColorValue):
    @classmethod
    def new(self, h: CSSNumericValue, w: CSSNumberish, b: CSSNumberish, alpha: CSSNumberish | None = 1) -> CSSHWB: ...
    h: CSSNumericValue
    w: CSSNumberish
    b: CSSNumberish
    alpha: CSSNumberish

class CSSLab(CSSColorValue):
    @classmethod
    def new(self, l: CSSColorPercent, a: CSSColorNumber, b: CSSColorNumber, alpha: CSSColorPercent | None = 1) -> CSSLab: ...
    l: CSSColorPercent
    a: CSSColorNumber
    b: CSSColorNumber
    alpha: CSSColorPercent

class CSSLCH(CSSColorValue):
    @classmethod
    def new(self, l: CSSColorPercent, c: CSSColorPercent, h: CSSColorAngle, alpha: CSSColorPercent | None = 1) -> CSSLCH: ...
    l: CSSColorPercent
    c: CSSColorPercent
    h: CSSColorAngle
    alpha: CSSColorPercent

class CSSOKLab(CSSColorValue):
    @classmethod
    def new(self, l: CSSColorPercent, a: CSSColorNumber, b: CSSColorNumber, alpha: CSSColorPercent | None = 1) -> CSSOKLab: ...
    l: CSSColorPercent
    a: CSSColorNumber
    b: CSSColorNumber
    alpha: CSSColorPercent

class CSSOKLCH(CSSColorValue):
    @classmethod
    def new(self, l: CSSColorPercent, c: CSSColorPercent, h: CSSColorAngle, alpha: CSSColorPercent | None = 1) -> CSSOKLCH: ...
    l: CSSColorPercent
    c: CSSColorPercent
    h: CSSColorAngle
    alpha: CSSColorPercent

class CSSColor(CSSColorValue):
    @classmethod
    def new(self, colorSpace: CSSKeywordish, channels: Sequence[CSSColorPercent], alpha: CSSNumberish | None = 1) -> CSSColor: ...
    colorSpace: CSSKeywordish
    channels: Sequence[CSSColorPercent]
    alpha: CSSNumberish

class ViewTransition:
    def skipTransition(self): ...
    finished: Awaitable[None]
    ready: Awaitable[None]
    updateCallbackDone: Awaitable[None]

class ScrollOptions(TypedDict):
    behavior: NotRequired[ScrollBehavior]

class ScrollToOptions(TypedDict, ScrollOptions):
    left: NotRequired[float]
    top: NotRequired[float]

class MediaQueryList(EventTarget):
    media: CSSOMString
    matches: bool
    def addListener(self, callback: EventListener | None): ...
    def removeListener(self, callback: EventListener | None): ...
    onchange: EventHandler

class MediaQueryListEvent(Event):
    @classmethod
    def new(self, type: CSSOMString, eventInitDict: MediaQueryListEventInit | None = {}) -> MediaQueryListEvent: ...
    media: CSSOMString
    matches: bool

class MediaQueryListEventInit(TypedDict, EventInit):
    media: NotRequired[CSSOMString]
    matches: NotRequired[bool]

class Screen:
    availWidth: int
    availHeight: int
    width: int
    height: int
    colorDepth: int
    pixelDepth: int
    orientation: ScreenOrientation
    isExtended: bool
    onchange: EventHandler

class CaretPosition:
    offsetNode: Node
    offset: int
    def getClientRect(self) -> DOMRect | None: ...

class ScrollIntoViewOptions(TypedDict, ScrollOptions):
    block: NotRequired[ScrollLogicalPosition]
    inline: NotRequired[ScrollLogicalPosition]

class CheckVisibilityOptions(TypedDict):
    checkOpacity: NotRequired[bool]
    checkVisibilityCSS: NotRequired[bool]

class HTMLElement(Element, ElementCSSInlineStyle, GlobalEventHandlers, ElementContentEditable, HTMLOrSVGElement):
    @classmethod
    def new(self) -> HTMLElement: ...
    offsetParent: Element | None
    offsetTop: int
    offsetLeft: int
    offsetWidth: int
    offsetHeight: int
    title: str
    lang: str
    translate: bool
    dir: str
    hidden: bool | float | str | None
    inert: bool
    def click(self): ...
    accessKey: str
    accessKeyLabel: str
    draggable: bool
    spellcheck: bool
    autocapitalize: str
    innerText: str
    outerText: str
    def attachInternals(self) -> ElementInternals: ...

class MouseEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: MouseEventInit | None = {}) -> MouseEvent: ...
    pageX: float
    pageY: float
    x: float
    y: float
    offsetX: float
    offsetY: float
    movementX: float
    movementY: float
    screenX: int
    screenY: int
    clientX: int
    clientY: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    button: short
    buttons: int
    relatedTarget: EventTarget | None
    def getModifierState(self, keyArg: str) -> bool: ...
    def initMouseEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: Window | None = None, detailArg: int | None = 0, screenXArg: int | None = 0, screenYArg: int | None = 0, clientXArg: int | None = 0, clientYArg: int | None = 0, ctrlKeyArg: bool | None = false, altKeyArg: bool | None = false, shiftKeyArg: bool | None = false, metaKeyArg: bool | None = false, buttonArg: short | None = 0, relatedTargetArg: EventTarget | None = None): ...

class BoxQuadOptions(TypedDict):
    box: NotRequired[CSSBoxType]
    relativeTo: NotRequired[GeometryNode]

class ConvertCoordinateOptions(TypedDict):
    fromBox: NotRequired[CSSBoxType]
    toBox: NotRequired[CSSBoxType]

class GeometryUtils:
    def getBoxQuads(self, options: BoxQuadOptions | None = {}) -> Sequence[DOMQuad]: ...
    def convertQuadFromNode(self, quad: DOMQuadInit, from_: GeometryNode, options: ConvertCoordinateOptions | None = {}) -> DOMQuad: ...
    def convertRectFromNode(self, rect: DOMRectReadOnly, from_: GeometryNode, options: ConvertCoordinateOptions | None = {}) -> DOMQuad: ...
    def convertPointFromNode(self, point: DOMPointInit, from_: GeometryNode, options: ConvertCoordinateOptions | None = {}) -> DOMPoint: ...

class Text(CharacterData, GeometryUtils, Slottable):
    @classmethod
    def new(self, data: str | None = "") -> Text: ...
    def splitText(self, offset: int) -> Text: ...
    wholeText: str

class VisualViewport(EventTarget):
    offsetLeft: float
    offsetTop: float
    pageLeft: float
    pageTop: float
    width: float
    height: float
    scale: float
    onresize: EventHandler
    onscroll: EventHandler
    onscrollend: EventHandler

class MediaList:
    mediaText: CSSOMString
    length: int
    def appendMedium(self, medium: CSSOMString): ...
    def deleteMedium(self, medium: CSSOMString): ...

class StyleSheet:
    type: CSSOMString
    href: USVString | None
    ownerNode: Element | ProcessingInstruction | None
    parentStyleSheet: CSSStyleSheet | None
    title: str | None
    media: MediaList
    disabled: bool

class CSSStyleSheet(StyleSheet):
    @classmethod
    def new(self, options: CSSStyleSheetInit | None = {}) -> CSSStyleSheet: ...
    ownerRule: CSSRule | None
    cssRules: CSSRuleList
    def insertRule(self, rule: CSSOMString, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...
    def replace(self, text: USVString) -> Awaitable[CSSStyleSheet]: ...
    def replaceSync(self, text: USVString): ...
    rules: CSSRuleList
    def addRule(self, selector: str | None = "undefined", style: str | None = "undefined", index: int | None = None) -> int: ...
    def removeRule(self, index: int | None = 0): ...

class CSSStyleSheetInit(TypedDict):
    baseURL: NotRequired[str]
    media: NotRequired[MediaList | str]
    disabled: NotRequired[bool]

class StyleSheetList:
    length: int

class DocumentOrShadowRoot:
    styleSheets: StyleSheetList
    adoptedStyleSheets: Sequence[CSSStyleSheet]
    fullscreenElement: Element | None
    activeElement: Element | None
    pictureInPictureElement: Element | None
    pointerLockElement: Element | None
    def getAnimations(self) -> Sequence[Animation]: ...

class LinkStyle:
    sheet: CSSStyleSheet | None

class ProcessingInstruction(CharacterData, LinkStyle):
    target: str

class CSSRuleList:
    length: int

class CSSGroupingRule(CSSRule):
    cssRules: CSSRuleList
    def insertRule(self, rule: CSSOMString, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...

class CSSPageRule(CSSGroupingRule):
    selectorText: CSSOMString
    style: CSSStyleDeclaration

class CSSMarginRule(CSSRule):
    name: CSSOMString
    style: CSSStyleDeclaration

class CSSNamespaceRule(CSSRule):
    namespaceURI: CSSOMString
    prefix: CSSOMString

class CSSStyleDeclaration:
    cssText: CSSOMString
    length: int
    def getPropertyValue(self, property: CSSOMString) -> CSSOMString: ...
    def getPropertyPriority(self, property: CSSOMString) -> CSSOMString: ...
    def setProperty(self, property: CSSOMString, value: CSSOMString, priority: CSSOMString | None = ""): ...
    def removeProperty(self, property: CSSOMString) -> CSSOMString: ...
    parentRule: CSSRule | None
    cssFloat: CSSOMString
    accentColor: str
    additiveSymbols: str
    alignContent: str
    alignItems: str
    alignSelf: str
    alignmentBaseline: str
    all: str
    animation: str
    animationComposition: str
    animationDelay: str
    animationDirection: str
    animationDuration: str
    animationFillMode: str
    animationIterationCount: str
    animationName: str
    animationPlayState: str
    animationTimingFunction: str
    appRegion: str
    appearance: str
    ascentOverride: str
    aspectRatio: str
    backdropFilter: str
    backfaceVisibility: str
    background: str
    backgroundAttachment: str
    backgroundBlendMode: str
    backgroundClip: str
    backgroundColor: str
    backgroundImage: str
    backgroundOrigin: str
    backgroundPosition: str
    backgroundPositionX: str
    backgroundPositionY: str
    backgroundRepeat: str
    backgroundRepeatX: str
    backgroundRepeatY: str
    backgroundSize: str
    basePalette: str
    baselineShift: str
    baselineSource: str
    blockSize: str
    border: str
    borderBlock: str
    borderBlockColor: str
    borderBlockEnd: str
    borderBlockEndColor: str
    borderBlockEndStyle: str
    borderBlockEndWidth: str
    borderBlockStart: str
    borderBlockStartColor: str
    borderBlockStartStyle: str
    borderBlockStartWidth: str
    borderBlockStyle: str
    borderBlockWidth: str
    borderBottom: str
    borderBottomColor: str
    borderBottomLeftRadius: str
    borderBottomRightRadius: str
    borderBottomStyle: str
    borderBottomWidth: str
    borderCollapse: str
    borderColor: str
    borderEndEndRadius: str
    borderEndStartRadius: str
    borderImage: str
    borderImageOutset: str
    borderImageRepeat: str
    borderImageSlice: str
    borderImageSource: str
    borderImageWidth: str
    borderInline: str
    borderInlineColor: str
    borderInlineEnd: str
    borderInlineEndColor: str
    borderInlineEndStyle: str
    borderInlineEndWidth: str
    borderInlineStart: str
    borderInlineStartColor: str
    borderInlineStartStyle: str
    borderInlineStartWidth: str
    borderInlineStyle: str
    borderInlineWidth: str
    borderLeft: str
    borderLeftColor: str
    borderLeftStyle: str
    borderLeftWidth: str
    borderRadius: str
    borderRight: str
    borderRightColor: str
    borderRightStyle: str
    borderRightWidth: str
    borderSpacing: str
    borderStartEndRadius: str
    borderStartStartRadius: str
    borderStyle: str
    borderTop: str
    borderTopColor: str
    borderTopLeftRadius: str
    borderTopRightRadius: str
    borderTopStyle: str
    borderTopWidth: str
    borderWidth: str
    bottom: str
    boxShadow: str
    boxSizing: str
    breakAfter: str
    breakBefore: str
    breakInside: str
    bufferedRendering: str
    captionSide: str
    caretColor: str
    clear: str
    clip: str
    clipPath: str
    clipRule: str
    color: str
    colorInterpolation: str
    colorInterpolationFilters: str
    colorRendering: str
    colorScheme: str
    columnCount: str
    columnFill: str
    columnGap: str
    columnRule: str
    columnRuleColor: str
    columnRuleStyle: str
    columnRuleWidth: str
    columnSpan: str
    columnWidth: str
    columns: str
    contain: str
    containIntrinsicBlockSize: str
    containIntrinsicHeight: str
    containIntrinsicInlineSize: str
    containIntrinsicSize: str
    containIntrinsicWidth: str
    container: str
    containerName: str
    containerType: str
    content: str
    contentVisibility: str
    counterIncrement: str
    counterReset: str
    counterSet: str
    cursor: str
    cx: str
    cy: str
    descentOverride: str
    direction: str
    display: str
    dominantBaseline: str
    emptyCells: str
    fallback: str
    fill: str
    fillOpacity: str
    fillRule: str
    filter: str
    flex: str
    flexBasis: str
    flexDirection: str
    flexFlow: str
    flexGrow: str
    flexShrink: str
    flexWrap: str
    floodColor: str
    floodOpacity: str
    font: str
    fontDisplay: str
    fontFamily: str
    fontFeatureSettings: str
    fontKerning: str
    fontOpticalSizing: str
    fontPalette: str
    fontSize: str
    fontStretch: str
    fontStyle: str
    fontSynthesis: str
    fontSynthesisSmallCaps: str
    fontSynthesisStyle: str
    fontSynthesisWeight: str
    fontVariant: str
    fontVariantAlternates: str
    fontVariantCaps: str
    fontVariantEastAsian: str
    fontVariantLigatures: str
    fontVariantNumeric: str
    fontVariationSettings: str
    fontWeight: str
    forcedColorAdjust: str
    gap: str
    grid: str
    gridArea: str
    gridAutoColumns: str
    gridAutoFlow: str
    gridAutoRows: str
    gridColumn: str
    gridColumnEnd: str
    gridColumnGap: str
    gridColumnStart: str
    gridGap: str
    gridRow: str
    gridRowEnd: str
    gridRowGap: str
    gridRowStart: str
    gridTemplate: str
    gridTemplateAreas: str
    gridTemplateColumns: str
    gridTemplateRows: str
    height: str
    hyphenateCharacter: str
    hyphenateLimitChars: str
    hyphens: str
    imageOrientation: str
    imageRendering: str
    inherits: str
    initialLetter: str
    initialValue: str
    inlineSize: str
    inset: str
    insetBlock: str
    insetBlockEnd: str
    insetBlockStart: str
    insetInline: str
    insetInlineEnd: str
    insetInlineStart: str
    isolation: str
    justifyContent: str
    justifyItems: str
    justifySelf: str
    left: str
    letterSpacing: str
    lightingColor: str
    lineBreak: str
    lineGapOverride: str
    lineHeight: str
    listStyle: str
    listStyleImage: str
    listStylePosition: str
    listStyleType: str
    margin: str
    marginBlock: str
    marginBlockEnd: str
    marginBlockStart: str
    marginBottom: str
    marginInline: str
    marginInlineEnd: str
    marginInlineStart: str
    marginLeft: str
    marginRight: str
    marginTop: str
    marker: str
    markerEnd: str
    markerMid: str
    markerStart: str
    mask: str
    maskType: str
    mathDepth: str
    mathShift: str
    mathStyle: str
    maxBlockSize: str
    maxHeight: str
    maxInlineSize: str
    maxWidth: str
    minBlockSize: str
    minHeight: str
    minInlineSize: str
    minWidth: str
    mixBlendMode: str
    negative: str
    objectFit: str
    objectPosition: str
    objectViewBox: str
    offset: str
    offsetDistance: str
    offsetPath: str
    offsetRotate: str
    opacity: str
    order: str
    orphans: str
    outline: str
    outlineColor: str
    outlineOffset: str
    outlineStyle: str
    outlineWidth: str
    overflow: str
    overflowAnchor: str
    overflowClipMargin: str
    overflowWrap: str
    overflowX: str
    overflowY: str
    overrideColors: str
    overscrollBehavior: str
    overscrollBehaviorBlock: str
    overscrollBehaviorInline: str
    overscrollBehaviorX: str
    overscrollBehaviorY: str
    pad: str
    padding: str
    paddingBlock: str
    paddingBlockEnd: str
    paddingBlockStart: str
    paddingBottom: str
    paddingInline: str
    paddingInlineEnd: str
    paddingInlineStart: str
    paddingLeft: str
    paddingRight: str
    paddingTop: str
    page: str
    pageBreakAfter: str
    pageBreakBefore: str
    pageBreakInside: str
    pageOrientation: str
    paintOrder: str
    perspective: str
    perspectiveOrigin: str
    placeContent: str
    placeItems: str
    placeSelf: str
    pointerEvents: str
    position: str
    prefix: str
    quotes: str
    range: str
    resize: str
    right: str
    rotate: str
    rowGap: str
    rubyPosition: str
    rx: str
    ry: str
    scale: str
    scrollBehavior: str
    scrollMargin: str
    scrollMarginBlock: str
    scrollMarginBlockEnd: str
    scrollMarginBlockStart: str
    scrollMarginBottom: str
    scrollMarginInline: str
    scrollMarginInlineEnd: str
    scrollMarginInlineStart: str
    scrollMarginLeft: str
    scrollMarginRight: str
    scrollMarginTop: str
    scrollPadding: str
    scrollPaddingBlock: str
    scrollPaddingBlockEnd: str
    scrollPaddingBlockStart: str
    scrollPaddingBottom: str
    scrollPaddingInline: str
    scrollPaddingInlineEnd: str
    scrollPaddingInlineStart: str
    scrollPaddingLeft: str
    scrollPaddingRight: str
    scrollPaddingTop: str
    scrollSnapAlign: str
    scrollSnapStop: str
    scrollSnapType: str
    scrollbarGutter: str
    shapeImageThreshold: str
    shapeMargin: str
    shapeOutside: str
    shapeRendering: str
    size: str
    sizeAdjust: str
    speak: str
    speakAs: str
    src: str
    stopColor: str
    stopOpacity: str
    stroke: str
    strokeDasharray: str
    strokeDashoffset: str
    strokeLinecap: str
    strokeLinejoin: str
    strokeMiterlimit: str
    strokeOpacity: str
    strokeWidth: str
    suffix: str
    symbols: str
    syntax: str
    system: str
    tabSize: str
    tableLayout: str
    textAlign: str
    textAlignLast: str
    textAnchor: str
    textCombineUpright: str
    textDecoration: str
    textDecorationColor: str
    textDecorationLine: str
    textDecorationSkipInk: str
    textDecorationStyle: str
    textDecorationThickness: str
    textEmphasis: str
    textEmphasisColor: str
    textEmphasisPosition: str
    textEmphasisStyle: str
    textIndent: str
    textOrientation: str
    textOverflow: str
    textRendering: str
    textShadow: str
    textSizeAdjust: str
    textTransform: str
    textUnderlineOffset: str
    textUnderlinePosition: str
    top: str
    touchAction: str
    transform: str
    transformBox: str
    transformOrigin: str
    transformStyle: str
    transition: str
    transitionDelay: str
    transitionDuration: str
    transitionProperty: str
    transitionTimingFunction: str
    translate: str
    unicodeBidi: str
    unicodeRange: str
    userSelect: str
    vectorEffect: str
    verticalAlign: str
    viewTransitionName: str
    visibility: str
    whiteSpace: str
    widows: str
    width: str
    willChange: str
    wordBreak: str
    wordSpacing: str
    wordWrap: str
    writingMode: str
    zIndex: str
    zoom: str

class MathMLElement(Element, ElementCSSInlineStyle, GlobalEventHandlers, HTMLOrSVGElement): ...

class ElementInternals(ARIAMixin):
    states: CustomStateSet
    shadowRoot: ShadowRoot | None
    def setFormValue(self, value: File | USVString | FormData | None, state: File | USVString | FormData | None = None): ...
    form: HTMLFormElement | None
    def setValidity(self, flags: ValidityStateFlags | None = {}, message: str | None = None, anchor: HTMLElement | None = None): ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    labels: NodeList

class CustomStateSet:
    def add(self, value: str): ...

class DataCue(TextTrackCue):
    @classmethod
    def new(self, startTime: float, endTime: float, value: Any, type: str | None = None) -> DataCue: ...
    value: Any
    type: str

class DeprecationReportBody(ReportBody):
    def toJSON(self) -> object: ...
    id: str
    anticipatedRemoval: object | None
    message: str
    sourceFile: str | None
    lineNumber: int | None
    columnNumber: int | None

class NavigatorDeviceMemory:
    deviceMemory: float

class DevicePosture(EventTarget):
    type: DevicePostureType
    onchange: EventHandler

class DigitalGoodsService:
    def getDetails(self, itemIds: Sequence[str]) -> Awaitable[Sequence[ItemDetails]]: ...
    def listPurchases(self) -> Awaitable[Sequence[PurchaseDetails]]: ...
    def listPurchaseHistory(self) -> Awaitable[Sequence[PurchaseDetails]]: ...
    def consume(self, purchaseToken: str) -> Awaitable[None]: ...

class ItemDetails(TypedDict):
    itemId: str
    title: str
    price: PaymentCurrencyAmount
    type: NotRequired[ItemType]
    description: NotRequired[str]
    iconURLs: NotRequired[Sequence[str]]
    subscriptionPeriod: NotRequired[str]
    freeTrialPeriod: NotRequired[str]
    introductoryPrice: NotRequired[PaymentCurrencyAmount]
    introductoryPricePeriod: NotRequired[str]
    introductoryPriceCycles: NotRequired[int]

class PurchaseDetails(TypedDict):
    itemId: str
    purchaseToken: str

class Event:
    @classmethod
    def new(self, type: str, eventInitDict: EventInit | None = {}) -> Event: ...
    type: str
    target: EventTarget | None
    srcElement: EventTarget | None
    currentTarget: EventTarget | None
    def composedPath(self) -> Sequence[EventTarget]: ...
    NONE = 0
    CAPTURING_PHASE = 1
    AT_TARGET = 2
    BUBBLING_PHASE = 3
    eventPhase: int
    def stopPropagation(self): ...
    cancelBubble: bool
    def stopImmediatePropagation(self): ...
    bubbles: bool
    cancelable: bool
    returnValue: bool
    def preventDefault(self): ...
    defaultPrevented: bool
    composed: bool
    isTrusted: bool
    timeStamp: DOMHighResTimeStamp
    def initEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false): ...

class EventInit(TypedDict):
    bubbles: NotRequired[bool]
    cancelable: NotRequired[bool]
    composed: NotRequired[bool]

class CustomEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: CustomEventInit | None = {}) -> CustomEvent: ...
    detail: Any
    def initCustomEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false, detail: Any | None = None): ...

class CustomEventInit(TypedDict, EventInit):
    detail: NotRequired[Any]

class EventTarget:
    @classmethod
    def new(self) -> EventTarget: ...
    def addEventListener(self, type: str, callback: EventListener | None, options: AddEventListenerOptions | bool | None = {}): ...
    def removeEventListener(self, type: str, callback: EventListener | None, options: EventListenerOptions | bool | None = {}): ...
    def dispatchEvent(self, event: Event) -> bool: ...

class EventListenerOptions(TypedDict):
    capture: NotRequired[bool]

class AddEventListenerOptions(TypedDict, EventListenerOptions):
    passive: NotRequired[bool]
    once: NotRequired[bool]
    signal: NotRequired[AbortSignal]

class AbortController:
    @classmethod
    def new(self) -> AbortController: ...
    signal: AbortSignal
    def abort(self, reason: Any | None = None): ...

class AbortSignal(EventTarget):
    aborted: bool
    reason: Any
    def throwIfAborted(self): ...
    onabort: EventHandler

class NonElementParentNode:
    def getElementById(self, elementId: str) -> Element | None: ...

class DocumentFragment(Node, NonElementParentNode, ParentNode):
    @classmethod
    def new(self) -> DocumentFragment: ...

class ParentNode:
    children: HTMLCollection
    firstElementChild: Element | None
    lastElementChild: Element | None
    childElementCount: int
    def prepend(self, *nodes: Node | str): ...
    def append(self, *nodes: Node | str): ...
    def replaceChildren(self, *nodes: Node | str): ...
    def querySelector(self, selectors: str) -> Element | None: ...
    def querySelectorAll(self, selectors: str) -> NodeList: ...

class NonDocumentTypeChildNode:
    previousElementSibling: Element | None
    nextElementSibling: Element | None

class CharacterData(Node, NonDocumentTypeChildNode, ChildNode):
    data: str
    length: int
    def substringData(self, offset: int, count: int) -> str: ...
    def appendData(self, data: str): ...
    def insertData(self, offset: int, data: str): ...
    def deleteData(self, offset: int, count: int): ...
    def replaceData(self, offset: int, count: int, data: str): ...

class ChildNode:
    def before(self, *nodes: Node | str): ...
    def after(self, *nodes: Node | str): ...
    def replaceWith(self, *nodes: Node | str): ...
    def remove(self): ...

class DocumentType(Node, ChildNode):
    name: str
    publicId: str
    systemId: str

class Slottable:
    assignedSlot: HTMLSlotElement | None

class NodeList:
    length: int

class HTMLCollection:
    length: int

class MutationObserver:
    @classmethod
    def new(self, callback: MutationCallback) -> MutationObserver: ...
    def observe(self, target: Node, options: MutationObserverInit | None = {}): ...
    def disconnect(self): ...
    def takeRecords(self) -> Sequence[MutationRecord]: ...

class MutationObserverInit(TypedDict):
    childList: NotRequired[bool]
    attributes: NotRequired[bool]
    characterData: NotRequired[bool]
    subtree: NotRequired[bool]
    attributeOldValue: NotRequired[bool]
    characterDataOldValue: NotRequired[bool]
    attributeFilter: NotRequired[Sequence[str]]

class MutationRecord:
    type: str
    target: Node
    addedNodes: NodeList
    removedNodes: NodeList
    previousSibling: Node | None
    nextSibling: Node | None
    attributeName: str | None
    attributeNamespace: str | None
    oldValue: str | None

class Node(EventTarget):
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12
    nodeType: int
    nodeName: str
    baseURI: USVString
    isConnected: bool
    ownerDocument: Document | None
    def getRootNode(self, options: GetRootNodeOptions | None = {}) -> Node: ...
    parentNode: Node | None
    parentElement: Element | None
    def hasChildNodes(self) -> bool: ...
    childNodes: NodeList
    firstChild: Node | None
    lastChild: Node | None
    previousSibling: Node | None
    nextSibling: Node | None
    nodeValue: str | None
    textContent: str | None
    def normalize(self): ...
    def cloneNode(self, deep: bool | None = false) -> Node: ...
    def isEqualNode(self, otherNode: Node | None) -> bool: ...
    def isSameNode(self, otherNode: Node | None) -> bool: ...
    DOCUMENT_POSITION_DISCONNECTED = 0x01
    DOCUMENT_POSITION_PRECEDING = 0x02
    DOCUMENT_POSITION_FOLLOWING = 0x04
    DOCUMENT_POSITION_CONTAINS = 0x08
    DOCUMENT_POSITION_CONTAINED_BY = 0x10
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = 0x20
    def compareDocumentPosition(self, other: Node) -> int: ...
    def contains(self, other: Node | None) -> bool: ...
    def lookupPrefix(self, namespace: str | None) -> str | None: ...
    def lookupNamespaceURI(self, prefix: str | None) -> str | None: ...
    def isDefaultNamespace(self, namespace: str | None) -> bool: ...
    def insertBefore(self, node: Node, child: Node | None) -> Node: ...
    def appendChild(self, node: Node) -> Node: ...
    def replaceChild(self, node: Node, child: Node) -> Node: ...
    def removeChild(self, child: Node) -> Node: ...

class GetRootNodeOptions(TypedDict):
    composed: NotRequired[bool]

class XMLDocument(Document): ...

class ElementCreationOptions(TypedDict): ...

class DOMImplementation:
    def createDocumentType(self, qualifiedName: str, publicId: str, systemId: str) -> DocumentType: ...
    def createDocument(self, namespace: str | None, qualifiedName: str, doctype: DocumentType | None = None) -> XMLDocument: ...
    def createHTMLDocument(self, title: str | None = None) -> Document: ...
    def hasFeature(self) -> bool: ...

class ShadowRootInit(TypedDict):
    mode: ShadowRootMode
    delegatesFocus: NotRequired[bool]
    slotAssignment: NotRequired[SlotAssignmentMode]

class NamedNodeMap:
    length: int
    def getNamedItemNS(self, namespace: str | None, localName: str) -> Attr | None: ...
    def setNamedItem(self, attr: Attr) -> Attr | None: ...
    def setNamedItemNS(self, attr: Attr) -> Attr | None: ...
    def removeNamedItem(self, qualifiedName: str) -> Attr: ...
    def removeNamedItemNS(self, namespace: str | None, localName: str) -> Attr: ...

class Attr(Node):
    namespaceURI: str | None
    prefix: str | None
    localName: str
    name: str
    value: str
    ownerElement: Element | None
    specified: bool

class CDATASection(Text): ...

class Comment(CharacterData):
    @classmethod
    def new(self, data: str | None = "") -> Comment: ...

class AbstractRange:
    startContainer: Node
    startOffset: int
    endContainer: Node
    endOffset: int
    collapsed: bool

class StaticRangeInit(TypedDict):
    startContainer: Node
    startOffset: int
    endContainer: Node
    endOffset: int

class StaticRange(AbstractRange):
    @classmethod
    def new(self, init: StaticRangeInit) -> StaticRange: ...

class NodeIterator:
    root: Node
    referenceNode: Node
    pointerBeforeReferenceNode: bool
    whatToShow: int
    filter: NodeFilter | None
    def nextNode(self) -> Node | None: ...
    def previousNode(self) -> Node | None: ...
    def detach(self): ...

class TreeWalker:
    root: Node
    whatToShow: int
    filter: NodeFilter | None
    currentNode: Node
    def parentNode(self) -> Node | None: ...
    def firstChild(self) -> Node | None: ...
    def lastChild(self) -> Node | None: ...
    def previousSibling(self) -> Node | None: ...
    def nextSibling(self) -> Node | None: ...
    def previousNode(self) -> Node | None: ...
    def nextNode(self) -> Node | None: ...

class DOMTokenList:
    length: int
    def contains(self, token: str) -> bool: ...
    def add(self, *tokens: str): ...
    def remove(self, *tokens: str): ...
    def toggle(self, token: str, force: bool | None = None) -> bool: ...
    def replace(self, token: str, newToken: str) -> bool: ...
    def supports(self, token: str) -> bool: ...
    value: str

class XPathResult:
    ANY_TYPE = 0
    NUMBER_TYPE = 1
    STRING_TYPE = 2
    BOOLEAN_TYPE = 3
    UNORDERED_NODE_ITERATOR_TYPE = 4
    ORDERED_NODE_ITERATOR_TYPE = 5
    UNORDERED_NODE_SNAPSHOT_TYPE = 6
    ORDERED_NODE_SNAPSHOT_TYPE = 7
    ANY_UNORDERED_NODE_TYPE = 8
    FIRST_ORDERED_NODE_TYPE = 9
    resultType: int
    numberValue: float
    stringValue: str
    booleanValue: bool
    singleNodeValue: Node | None
    invalidIteratorState: bool
    snapshotLength: int
    def iterateNext(self) -> Node | None: ...
    def snapshotItem(self, index: int) -> Node | None: ...

class XPathExpression:
    def evaluate(self, contextNode: Node, type: int | None = 0, result: XPathResult | None = None) -> XPathResult: ...

class XPathEvaluatorBase:
    def createExpression(self, expression: str, resolver: XPathNSResolver | None = None) -> XPathExpression: ...
    def createNSResolver(self, nodeResolver: Node) -> XPathNSResolver: ...
    def evaluate(self, expression: str, contextNode: Node, resolver: XPathNSResolver | None = None, type: int | None = 0, result: XPathResult | None = None) -> XPathResult: ...

class XPathEvaluator(XPathEvaluatorBase):
    @classmethod
    def new(self) -> XPathEvaluator: ...

class XSLTProcessor:
    @classmethod
    def new(self) -> XSLTProcessor: ...
    def importStylesheet(self, style: Node): ...
    def transformToFragment(self, source: Node, output: Document) -> DocumentFragment: ...
    def transformToDocument(self, source: Node) -> Document: ...
    def setParameter(self, namespaceURI: str, localName: str, value: Any): ...
    def getParameter(self, namespaceURI: str, localName: str) -> Any: ...
    def removeParameter(self, namespaceURI: str, localName: str): ...
    def clearParameters(self): ...
    def reset(self): ...

class EditContextInit(TypedDict):
    text: NotRequired[str]
    selectionStart: NotRequired[int]
    selectionEnd: NotRequired[int]

class EditContext(EventTarget):
    @classmethod
    def new(self, options: EditContextInit | None = {}) -> EditContext: ...
    def updateText(self, rangeStart: int, rangeEnd: int, text: str): ...
    def updateSelection(self, start: int, end: int): ...
    def updateControlBound(self, controlBound: DOMRect): ...
    def updateSelectionBound(self, selectionBound: DOMRect): ...
    def updateCharacterBounds(self, rangeStart: int, characterBounds: Sequence[DOMRect]): ...
    def attachedElements(self) -> Sequence[Element]: ...
    text: str
    selectionStart: int
    selectionEnd: int
    compositionRangeStart: int
    compositionRangeEnd: int
    isInComposition: bool
    controlBound: DOMRect
    selectionBound: DOMRect
    characterBoundsRangeStart: int
    def characterBounds(self) -> Sequence[DOMRect]: ...
    ontextupdate: EventHandler
    ontextformatupdate: EventHandler
    oncharacterboundsupdate: EventHandler
    oncompositionstart: EventHandler
    oncompositionend: EventHandler

class TextUpdateEventInit(TypedDict):
    updateRangeStart: NotRequired[int]
    updateRangeEnd: NotRequired[int]
    text: NotRequired[str]
    selectionStart: NotRequired[int]
    selectionEnd: NotRequired[int]
    compositionStart: NotRequired[int]
    compositionEnd: NotRequired[int]

class TextUpdateEvent(Event):
    @classmethod
    def new(self, options: TextUpdateEventInit | None = {}) -> TextUpdateEvent: ...
    updateRangeStart: int
    updateRangeEnd: int
    text: str
    selectionStart: int
    selectionEnd: int
    compositionStart: int
    compositionEnd: int

class TextFormatInit(TypedDict):
    rangeStart: NotRequired[int]
    rangeEnd: NotRequired[int]
    textColor: NotRequired[str]
    backgroundColor: NotRequired[str]
    underlineStyle: NotRequired[str]
    underlineThickness: NotRequired[str]
    underlineColor: NotRequired[str]

class TextFormat:
    @classmethod
    def new(self, options: TextFormatInit | None = {}) -> TextFormat: ...
    rangeStart: int
    rangeEnd: int
    textColor: str
    backgroundColor: str
    underlineStyle: str
    underlineThickness: str
    underlineColor: str

class TextFormatUpdateEventInit(TypedDict):
    textFormats: NotRequired[Sequence[TextFormat]]

class TextFormatUpdateEvent(Event):
    @classmethod
    def new(self, options: TextFormatUpdateEventInit | None = {}) -> TextFormatUpdateEvent: ...
    def getTextFormats(self) -> Sequence[TextFormat]: ...

class CharacterBoundsUpdateEventInit(TypedDict):
    rangeStart: NotRequired[int]
    rangeEnd: NotRequired[int]

class CharacterBoundsUpdateEvent(Event):
    @classmethod
    def new(self, options: CharacterBoundsUpdateEventInit | None = {}) -> CharacterBoundsUpdateEvent: ...
    rangeStart: int
    rangeEnd: int

class PerformanceElementTiming(PerformanceEntry):
    renderTime: DOMHighResTimeStamp
    loadTime: DOMHighResTimeStamp
    intersectionRect: DOMRectReadOnly
    identifier: str
    naturalWidth: int
    naturalHeight: int
    id: str
    element: Element | None
    url: str
    def toJSON(self) -> object: ...

class TextDecoderCommon:
    encoding: str
    fatal: bool
    ignoreBOM: bool

class TextDecoderOptions(TypedDict):
    fatal: NotRequired[bool]
    ignoreBOM: NotRequired[bool]

class TextDecodeOptions(TypedDict):
    stream: NotRequired[bool]

class TextDecoder(TextDecoderCommon):
    @classmethod
    def new(self, label: str | None = "utf-8", options: TextDecoderOptions | None = {}) -> TextDecoder: ...
    def decode(self, input: BufferSource | None = None, options: TextDecodeOptions | None = {}) -> USVString: ...

class TextEncoderCommon:
    encoding: str

class TextEncoderEncodeIntoResult(TypedDict):
    read: NotRequired[int]
    written: NotRequired[int]

class TextEncoder(TextEncoderCommon):
    @classmethod
    def new(self) -> TextEncoder: ...
    def encode(self, input: USVString | None = "") -> Uint8Array: ...
    def encodeInto(self, source: USVString, destination: Uint8Array) -> TextEncoderEncodeIntoResult: ...

class TextDecoderStream(TextDecoderCommon, GenericTransformStream):
    @classmethod
    def new(self, label: str | None = "utf-8", options: TextDecoderOptions | None = {}) -> TextDecoderStream: ...

class TextEncoderStream(TextEncoderCommon, GenericTransformStream):
    @classmethod
    def new(self) -> TextEncoderStream: ...

class MediaKeySystemConfiguration(TypedDict):
    label: NotRequired[str]
    initDataTypes: NotRequired[Sequence[str]]
    audioCapabilities: NotRequired[Sequence[MediaKeySystemMediaCapability]]
    videoCapabilities: NotRequired[Sequence[MediaKeySystemMediaCapability]]
    distinctiveIdentifier: NotRequired[MediaKeysRequirement]
    persistentState: NotRequired[MediaKeysRequirement]
    sessionTypes: NotRequired[Sequence[str]]

class MediaKeySystemMediaCapability(TypedDict):
    contentType: NotRequired[str]
    encryptionScheme: NotRequired[str | None]
    robustness: NotRequired[str]

class MediaKeySystemAccess:
    keySystem: str
    def getConfiguration(self) -> MediaKeySystemConfiguration: ...
    def createMediaKeys(self) -> Awaitable[MediaKeys]: ...

class MediaKeys:
    def createSession(self, sessionType: MediaKeySessionType | None = "temporary") -> MediaKeySession: ...
    def setServerCertificate(self, serverCertificate: BufferSource) -> Awaitable[bool]: ...

class MediaKeySession(EventTarget):
    sessionId: str
    expiration: float
    closed: Awaitable[MediaKeySessionClosedReason]
    keyStatuses: MediaKeyStatusMap
    onkeystatuseschange: EventHandler
    onmessage: EventHandler
    def generateRequest(self, initDataType: str, initData: BufferSource) -> Awaitable[None]: ...
    def load(self, sessionId: str) -> Awaitable[bool]: ...
    def update(self, response: BufferSource) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def remove(self) -> Awaitable[None]: ...

class MediaKeyStatusMap:
    size: int
    def has(self, keyId: BufferSource) -> bool: ...
    def get(self, keyId: BufferSource) -> MediaKeyStatus | None: ...

class MediaKeyMessageEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: MediaKeyMessageEventInit) -> MediaKeyMessageEvent: ...
    messageType: MediaKeyMessageType
    message: ArrayBuffer

class MediaKeyMessageEventInit(TypedDict, EventInit):
    messageType: MediaKeyMessageType
    message: ArrayBuffer

class MediaEncryptedEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: MediaEncryptedEventInit | None = {}) -> MediaEncryptedEvent: ...
    initDataType: str
    initData: ArrayBuffer

class MediaEncryptedEventInit(TypedDict, EventInit):
    initDataType: NotRequired[str]
    initData: NotRequired[ArrayBuffer]

class HTMLInputElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLInputElement: ...
    webkitdirectory: bool
    webkitEntries: Sequence[FileSystemEntry]
    capture: str
    accept: str
    alt: str
    autocomplete: str
    defaultChecked: bool
    checked: bool
    dirName: str
    disabled: bool
    form: HTMLFormElement | None
    files: FileList | None
    formAction: USVString
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    height: int
    indeterminate: bool
    list: HTMLDataListElement | None
    max: str
    maxLength: int
    min: str
    minLength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readOnly: bool
    required: bool
    size: int
    src: USVString
    step: str
    type: str
    defaultValue: str
    value: str
    valueAsDate: object | None
    valueAsNumber: float
    width: int
    def stepUp(self, n: int | None = 1): ...
    def stepDown(self, n: int | None = 1): ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList | None
    def select(self): ...
    selectionStart: int | None
    selectionEnd: int | None
    selectionDirection: str | None
    @overload
    def setRangeText(self, replacement: str): ...
    @overload
    def setRangeText(self, replacement: str, start: int, end: int, selectionMode: SelectionMode | None = "preserve"): ...
    def setSelectionRange(self, start: int, end: int, direction: str | None = None): ...
    def showPicker(self): ...
    align: str
    useMap: str

class DataTransferItem:
    def webkitGetAsEntry(self) -> FileSystemEntry | None: ...
    def getAsFileSystemHandle(self) -> Awaitable[FileSystemHandle | None]: ...
    kind: str
    type: str
    def getAsString(self, callback: FunctionStringCallback | None): ...
    def getAsFile(self) -> File | None: ...

class FileSystemEntry:
    isFile: bool
    isDirectory: bool
    name: USVString
    fullPath: USVString
    filesystem: FileSystem
    def getParent(self, successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...

class FileSystemDirectoryEntry(FileSystemEntry):
    def createReader(self) -> FileSystemDirectoryReader: ...
    def getFile(self, path: USVString | None = None, options: FileSystemFlags | None = {}, successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...
    def getDirectory(self, path: USVString | None = None, options: FileSystemFlags | None = {}, successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...

class FileSystemFlags(TypedDict):
    create: NotRequired[bool]
    exclusive: NotRequired[bool]

class FileSystemDirectoryReader:
    def readEntries(self, successCallback: FileSystemEntriesCallback, errorCallback: ErrorCallback | None = None): ...

class FileSystemFileEntry(FileSystemEntry):
    def file(self, successCallback: FileCallback, errorCallback: ErrorCallback | None = None): ...

class FileSystem:
    name: USVString
    root: FileSystemDirectoryEntry

class EpubReadingSystem:
    def hasFeature(self, feature: str, version: str | None = None) -> bool: ...

class PerformanceEventTiming(PerformanceEntry):
    processingStart: DOMHighResTimeStamp
    processingEnd: DOMHighResTimeStamp
    cancelable: bool
    target: Node | None
    interactionId: int
    def toJSON(self) -> object: ...

class EventCounts: ...

class Performance(EventTarget):
    eventCounts: EventCounts
    interactionCount: int
    def now(self) -> DOMHighResTimeStamp: ...
    timeOrigin: DOMHighResTimeStamp
    def toJSON(self) -> object: ...
    timing: PerformanceTiming
    navigation: PerformanceNavigation
    def measureUserAgentSpecificMemory(self) -> Awaitable[MemoryMeasurement]: ...
    def getEntries(self) -> PerformanceEntryList: ...
    def getEntriesByType(self, type: str) -> PerformanceEntryList: ...
    def getEntriesByName(self, name: str, type: str | None = None) -> PerformanceEntryList: ...
    def clearResourceTimings(self): ...
    def setResourceTimingBufferSize(self, maxSize: int): ...
    onresourcetimingbufferfull: EventHandler
    def mark(self, markName: str, markOptions: PerformanceMarkOptions | None = {}) -> PerformanceMark: ...
    def clearMarks(self, markName: str | None = None): ...
    def measure(self, measureName: str, startOrMeasureOptions: str | PerformanceMeasureOptions | None = {}, endMark: str | None = None) -> PerformanceMeasure: ...
    def clearMeasures(self, measureName: str | None = None): ...

class PerformanceObserverInit(TypedDict, TypedDict):
    durationThreshold: NotRequired[DOMHighResTimeStamp]
    entryTypes: NotRequired[Sequence[str]]
    type: NotRequired[str]
    buffered: NotRequired[bool]

class ColorSelectionResult(TypedDict):
    sRGBHex: NotRequired[str]

class ColorSelectionOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class EyeDropper:
    @classmethod
    def new(self) -> EyeDropper: ...
    def open(self, options: ColorSelectionOptions | None = {}) -> Awaitable[ColorSelectionResult]: ...

class Headers:
    @classmethod
    def new(self, init: HeadersInit | None = None) -> Headers: ...
    def append(self, name: ByteString, value: ByteString): ...
    def delete(self, name: ByteString): ...
    def get(self, name: ByteString) -> ByteString | None: ...
    def has(self, name: ByteString) -> bool: ...
    def set(self, name: ByteString, value: ByteString): ...

class Body:
    body: ReadableStream | None
    bodyUsed: bool
    def arrayBuffer(self) -> Awaitable[ArrayBuffer]: ...
    def blob(self) -> Awaitable[Blob]: ...
    def formData(self) -> Awaitable[FormData]: ...
    def json(self) -> Awaitable[Any]: ...
    def text(self) -> Awaitable[USVString]: ...

class Request(Body):
    @classmethod
    def new(self, input: RequestInfo, init: RequestInit | None = {}) -> Request: ...
    method: ByteString
    url: USVString
    headers: Headers
    destination: RequestDestination
    referrer: USVString
    referrerPolicy: ReferrerPolicy
    mode: RequestMode
    credentials: RequestCredentials
    cache: RequestCache
    redirect: RequestRedirect
    integrity: str
    keepalive: bool
    isReloadNavigation: bool
    isHistoryNavigation: bool
    signal: AbortSignal
    duplex: RequestDuplex
    def clone(self) -> Request: ...

class RequestInit(TypedDict):
    method: NotRequired[ByteString]
    headers: NotRequired[HeadersInit]
    body: NotRequired[BodyInit | None]
    referrer: NotRequired[USVString]
    referrerPolicy: NotRequired[ReferrerPolicy]
    mode: NotRequired[RequestMode]
    credentials: NotRequired[RequestCredentials]
    cache: NotRequired[RequestCache]
    redirect: NotRequired[RequestRedirect]
    integrity: NotRequired[str]
    keepalive: NotRequired[bool]
    signal: NotRequired[AbortSignal | None]
    duplex: NotRequired[RequestDuplex]
    priority: NotRequired[RequestPriority]
    window: NotRequired[Any]

class Response(Body):
    @classmethod
    def new(self, body: BodyInit | None = None, init: ResponseInit | None = {}) -> Response: ...
    type: ResponseType
    url: USVString
    redirected: bool
    status: int
    ok: bool
    statusText: ByteString
    headers: Headers
    def clone(self) -> Response: ...

class ResponseInit(TypedDict):
    status: NotRequired[int]
    statusText: NotRequired[ByteString]
    headers: NotRequired[HeadersInit]

class AuthenticationExtensionsClientInputs(TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict):
    credentialProtectionPolicy: NotRequired[USVString]
    enforceCredentialProtectionPolicy: NotRequired[bool]
    credBlob: NotRequired[ArrayBuffer]
    getCredBlob: NotRequired[bool]
    minPinLength: NotRequired[bool]
    hmacCreateSecret: NotRequired[bool]
    hmacGetSecret: NotRequired[HMACGetSecretInput]
    payment: NotRequired[AuthenticationExtensionsPaymentInputs]
    appid: NotRequired[USVString]
    appidExclude: NotRequired[USVString]
    credProps: NotRequired[bool]
    prf: NotRequired[AuthenticationExtensionsPRFInputs]
    largeBlob: NotRequired[AuthenticationExtensionsLargeBlobInputs]
    uvm: NotRequired[bool]
    devicePubKey: NotRequired[AuthenticationExtensionsDevicePublicKeyInputs]

class HMACGetSecretInput(TypedDict):
    salt1: ArrayBuffer
    salt2: NotRequired[ArrayBuffer]

class AuthenticationExtensionsClientOutputs(TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict, TypedDict):
    hmacCreateSecret: NotRequired[bool]
    hmacGetSecret: NotRequired[HMACGetSecretOutput]
    appid: NotRequired[bool]
    appidExclude: NotRequired[bool]
    credProps: NotRequired[CredentialPropertiesOutput]
    prf: NotRequired[AuthenticationExtensionsPRFOutputs]
    largeBlob: NotRequired[AuthenticationExtensionsLargeBlobOutputs]
    uvm: NotRequired[UvmEntries]
    devicePubKey: NotRequired[AuthenticationExtensionsDevicePublicKeyOutputs]

class HMACGetSecretOutput(TypedDict):
    output1: ArrayBuffer
    output2: NotRequired[ArrayBuffer]

class FileSystemPermissionDescriptor(TypedDict, PermissionDescriptor):
    handle: FileSystemHandle
    mode: NotRequired[FileSystemPermissionMode]

class FileSystemHandlePermissionDescriptor(TypedDict):
    mode: NotRequired[FileSystemPermissionMode]

class FileSystemHandle:
    def queryPermission(self, descriptor: FileSystemHandlePermissionDescriptor | None = {}) -> Awaitable[PermissionState]: ...
    def requestPermission(self, descriptor: FileSystemHandlePermissionDescriptor | None = {}) -> Awaitable[PermissionState]: ...
    kind: FileSystemHandleKind
    name: USVString
    def isSameEntry(self, other: FileSystemHandle) -> Awaitable[bool]: ...

class FilePickerAcceptType(TypedDict):
    description: NotRequired[USVString]
    accept: NotRequired[USVString | Sequence[USVString]]

class FilePickerOptions(TypedDict):
    types: NotRequired[Sequence[FilePickerAcceptType]]
    excludeAcceptAllOption: NotRequired[bool]
    id: NotRequired[str]
    startIn: NotRequired[StartInDirectory]

class OpenFilePickerOptions(TypedDict, FilePickerOptions):
    multiple: NotRequired[bool]

class SaveFilePickerOptions(TypedDict, FilePickerOptions):
    suggestedName: NotRequired[USVString | None]

class DirectoryPickerOptions(TypedDict):
    id: NotRequired[str]
    startIn: NotRequired[StartInDirectory]
    mode: NotRequired[FileSystemPermissionMode]

class SVGFilterElement(SVGElement, SVGURIReference):
    filterUnits: SVGAnimatedEnumeration
    primitiveUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGFilterPrimitiveStandardAttributes:
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    result: SVGAnimatedString

class SVGFEBlendElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_FEBLEND_MODE_UNKNOWN = 0
    SVG_FEBLEND_MODE_NORMAL = 1
    SVG_FEBLEND_MODE_MULTIPLY = 2
    SVG_FEBLEND_MODE_SCREEN = 3
    SVG_FEBLEND_MODE_DARKEN = 4
    SVG_FEBLEND_MODE_LIGHTEN = 5
    SVG_FEBLEND_MODE_OVERLAY = 6
    SVG_FEBLEND_MODE_COLOR_DODGE = 7
    SVG_FEBLEND_MODE_COLOR_BURN = 8
    SVG_FEBLEND_MODE_HARD_LIGHT = 9
    SVG_FEBLEND_MODE_SOFT_LIGHT = 10
    SVG_FEBLEND_MODE_DIFFERENCE = 11
    SVG_FEBLEND_MODE_EXCLUSION = 12
    SVG_FEBLEND_MODE_HUE = 13
    SVG_FEBLEND_MODE_SATURATION = 14
    SVG_FEBLEND_MODE_COLOR = 15
    SVG_FEBLEND_MODE_LUMINOSITY = 16
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    mode: SVGAnimatedEnumeration

class SVGFEColorMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_FECOLORMATRIX_TYPE_UNKNOWN = 0
    SVG_FECOLORMATRIX_TYPE_MATRIX = 1
    SVG_FECOLORMATRIX_TYPE_SATURATE = 2
    SVG_FECOLORMATRIX_TYPE_HUEROTATE = 3
    SVG_FECOLORMATRIX_TYPE_LUMINANCETOALPHA = 4
    in1: SVGAnimatedString
    type: SVGAnimatedEnumeration
    values: SVGAnimatedNumberList

class SVGFEComponentTransferElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class SVGComponentTransferFunctionElement(SVGElement):
    SVG_FECOMPONENTTRANSFER_TYPE_UNKNOWN = 0
    SVG_FECOMPONENTTRANSFER_TYPE_IDENTITY = 1
    SVG_FECOMPONENTTRANSFER_TYPE_TABLE = 2
    SVG_FECOMPONENTTRANSFER_TYPE_DISCRETE = 3
    SVG_FECOMPONENTTRANSFER_TYPE_LINEAR = 4
    SVG_FECOMPONENTTRANSFER_TYPE_GAMMA = 5
    type: SVGAnimatedEnumeration
    tableValues: SVGAnimatedNumberList
    slope: SVGAnimatedNumber
    intercept: SVGAnimatedNumber
    amplitude: SVGAnimatedNumber
    exponent: SVGAnimatedNumber
    offset: SVGAnimatedNumber

class SVGFEFuncRElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncGElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncBElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncAElement(SVGComponentTransferFunctionElement): ...

class SVGFECompositeElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_FECOMPOSITE_OPERATOR_UNKNOWN = 0
    SVG_FECOMPOSITE_OPERATOR_OVER = 1
    SVG_FECOMPOSITE_OPERATOR_IN = 2
    SVG_FECOMPOSITE_OPERATOR_OUT = 3
    SVG_FECOMPOSITE_OPERATOR_ATOP = 4
    SVG_FECOMPOSITE_OPERATOR_XOR = 5
    SVG_FECOMPOSITE_OPERATOR_ARITHMETIC = 6
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    k1: SVGAnimatedNumber
    k2: SVGAnimatedNumber
    k3: SVGAnimatedNumber
    k4: SVGAnimatedNumber

class SVGFEConvolveMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_EDGEMODE_UNKNOWN = 0
    SVG_EDGEMODE_DUPLICATE = 1
    SVG_EDGEMODE_WRAP = 2
    SVG_EDGEMODE_NONE = 3
    in1: SVGAnimatedString
    orderX: SVGAnimatedInteger
    orderY: SVGAnimatedInteger
    kernelMatrix: SVGAnimatedNumberList
    divisor: SVGAnimatedNumber
    bias: SVGAnimatedNumber
    targetX: SVGAnimatedInteger
    targetY: SVGAnimatedInteger
    edgeMode: SVGAnimatedEnumeration
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber
    preserveAlpha: SVGAnimatedBoolean

class SVGFEDiffuseLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    diffuseConstant: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class SVGFEDistantLightElement(SVGElement):
    azimuth: SVGAnimatedNumber
    elevation: SVGAnimatedNumber

class SVGFEPointLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber

class SVGFESpotLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber
    pointsAtX: SVGAnimatedNumber
    pointsAtY: SVGAnimatedNumber
    pointsAtZ: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    limitingConeAngle: SVGAnimatedNumber

class SVGFEDisplacementMapElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_CHANNEL_UNKNOWN = 0
    SVG_CHANNEL_R = 1
    SVG_CHANNEL_G = 2
    SVG_CHANNEL_B = 3
    SVG_CHANNEL_A = 4
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    scale: SVGAnimatedNumber
    xChannelSelector: SVGAnimatedEnumeration
    yChannelSelector: SVGAnimatedEnumeration

class SVGFEDropShadowElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber
    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float): ...

class SVGFEFloodElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGFEGaussianBlurElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_EDGEMODE_UNKNOWN = 0
    SVG_EDGEMODE_DUPLICATE = 1
    SVG_EDGEMODE_WRAP = 2
    SVG_EDGEMODE_NONE = 3
    in1: SVGAnimatedString
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber
    edgeMode: SVGAnimatedEnumeration
    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float): ...

class SVGFEImageElement(SVGElement, SVGFilterPrimitiveStandardAttributes, SVGURIReference):
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio
    crossOrigin: SVGAnimatedString

class SVGFEMergeElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGFEMergeNodeElement(SVGElement):
    in1: SVGAnimatedString

class SVGFEMorphologyElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_MORPHOLOGY_OPERATOR_UNKNOWN = 0
    SVG_MORPHOLOGY_OPERATOR_ERODE = 1
    SVG_MORPHOLOGY_OPERATOR_DILATE = 2
    in1: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    radiusX: SVGAnimatedNumber
    radiusY: SVGAnimatedNumber

class SVGFEOffsetElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber

class SVGFESpecularLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    specularConstant: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class SVGFETileElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class SVGFETurbulenceElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_TURBULENCE_TYPE_UNKNOWN = 0
    SVG_TURBULENCE_TYPE_FRACTALNOISE = 1
    SVG_TURBULENCE_TYPE_TURBULENCE = 2
    SVG_STITCHTYPE_UNKNOWN = 0
    SVG_STITCHTYPE_STITCH = 1
    SVG_STITCHTYPE_NOSTITCH = 2
    baseFrequencyX: SVGAnimatedNumber
    baseFrequencyY: SVGAnimatedNumber
    numOctaves: SVGAnimatedInteger
    seed: SVGAnimatedNumber
    stitchTiles: SVGAnimatedEnumeration
    type: SVGAnimatedEnumeration

class FontMetrics:
    width: float
    advances: Sequence[float]
    boundingBoxLeft: float
    boundingBoxRight: float
    height: float
    emHeightAscent: float
    emHeightDescent: float
    boundingBoxAscent: float
    boundingBoxDescent: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    dominantBaseline: Baseline
    baselines: Sequence[Baseline]
    fonts: Sequence[Font]

class Baseline:
    name: str
    value: float

class Font:
    name: str
    glyphsRendered: int

class FileSystemCreateWritableOptions(TypedDict):
    keepExistingData: NotRequired[bool]

class FileSystemFileHandle(FileSystemHandle):
    def getFile(self) -> Awaitable[File]: ...
    def createWritable(self, options: FileSystemCreateWritableOptions | None = {}) -> Awaitable[FileSystemWritableFileStream]: ...
    def createSyncAccessHandle(self) -> Awaitable[FileSystemSyncAccessHandle]: ...

class FileSystemGetFileOptions(TypedDict):
    create: NotRequired[bool]

class FileSystemGetDirectoryOptions(TypedDict):
    create: NotRequired[bool]

class FileSystemRemoveOptions(TypedDict):
    recursive: NotRequired[bool]

class FileSystemDirectoryHandle(FileSystemHandle):
    def getFileHandle(self, name: USVString, options: FileSystemGetFileOptions | None = {}) -> Awaitable[FileSystemFileHandle]: ...
    def getDirectoryHandle(self, name: USVString, options: FileSystemGetDirectoryOptions | None = {}) -> Awaitable[FileSystemDirectoryHandle]: ...
    def removeEntry(self, name: USVString, options: FileSystemRemoveOptions | None = {}) -> Awaitable[None]: ...
    def resolve(self, possibleDescendant: FileSystemHandle) -> Awaitable[Sequence[USVString]]: ...

class WriteParams(TypedDict):
    type: WriteCommandType
    size: NotRequired[int | None]
    position: NotRequired[int | None]
    data: NotRequired[BufferSource | Blob | USVString | None]

class FileSystemWritableFileStream(WritableStream):
    def write(self, data: FileSystemWriteChunkType) -> Awaitable[None]: ...
    def seek(self, position: int) -> Awaitable[None]: ...
    def truncate(self, size: int) -> Awaitable[None]: ...

class FileSystemReadWriteOptions(TypedDict):
    at: NotRequired[int]

class FileSystemSyncAccessHandle:
    def read(self, buffer: BufferSource, options: FileSystemReadWriteOptions | None = {}) -> int: ...
    def write(self, buffer: BufferSource, options: FileSystemReadWriteOptions | None = {}) -> int: ...
    def truncate(self, newSize: int): ...
    def getSize(self) -> int: ...
    def flush(self): ...
    def close(self): ...

class StorageManager:
    def getDirectory(self) -> Awaitable[FileSystemDirectoryHandle]: ...
    def persisted(self) -> Awaitable[bool]: ...
    def persist(self) -> Awaitable[bool]: ...
    def estimate(self) -> Awaitable[StorageEstimate]: ...

class FullscreenOptions(TypedDict, TypedDict):
    navigationUI: NotRequired[FullscreenNavigationUI]
    screen: NotRequired[ScreenDetailed]

class GamepadHapticActuator:
    type: GamepadHapticActuatorType
    def canPlayEffectType(self, type: GamepadHapticEffectType) -> bool: ...
    def playEffect(self, type: GamepadHapticEffectType, params: GamepadEffectParameters | None = {}) -> Awaitable[GamepadHapticsResult]: ...
    def pulse(self, value: float, duration: float) -> Awaitable[bool]: ...
    def reset(self) -> Awaitable[GamepadHapticsResult]: ...

class GamepadEffectParameters(TypedDict):
    duration: NotRequired[float]
    startDelay: NotRequired[float]
    strongMagnitude: NotRequired[float]
    weakMagnitude: NotRequired[float]

class GamepadPose:
    hasOrientation: bool
    hasPosition: bool
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array

class GamepadTouch:
    touchId: int
    surfaceId: octet
    position: Float32Array
    surfaceDimensions: Uint32Array

class Gamepad:
    hand: GamepadHand
    hapticActuators: Sequence[GamepadHapticActuator]
    pose: GamepadPose | None
    touchEvents: Sequence[GamepadTouch]
    vibrationActuator: GamepadHapticActuator
    id: str
    index: int
    connected: bool
    timestamp: DOMHighResTimeStamp
    mapping: GamepadMappingType
    axes: Sequence[float]
    buttons: Sequence[GamepadButton]

class GamepadButton:
    pressed: bool
    touched: bool
    value: float

class GamepadEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: GamepadEventInit) -> GamepadEvent: ...
    gamepad: Gamepad

class GamepadEventInit(TypedDict, EventInit):
    gamepad: Gamepad

class WindowEventHandlers:
    ongamepadconnected: EventHandler
    ongamepaddisconnected: EventHandler
    onafterprint: EventHandler
    onbeforeprint: EventHandler
    onbeforeunload: OnBeforeUnloadEventHandler
    onhashchange: EventHandler
    onlanguagechange: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler
    onoffline: EventHandler
    ononline: EventHandler
    onpagehide: EventHandler
    onpageshow: EventHandler
    onpopstate: EventHandler
    onrejectionhandled: EventHandler
    onstorage: EventHandler
    onunhandledrejection: EventHandler
    onunload: EventHandler
    onportalactivate: EventHandler

class Sensor(EventTarget):
    activated: bool
    hasReading: bool
    timestamp: DOMHighResTimeStamp | None
    def start(self): ...
    def stop(self): ...
    onreading: EventHandler
    onactivate: EventHandler
    onerror: EventHandler

class SensorOptions(TypedDict):
    frequency: NotRequired[float]

class SensorErrorEvent(Event):
    @classmethod
    def new(self, type: str, errorEventInitDict: SensorErrorEventInit) -> SensorErrorEvent: ...
    error: DOMException

class SensorErrorEventInit(TypedDict, EventInit):
    error: DOMException

class MockSensorConfiguration(TypedDict):
    mockSensorType: MockSensorType
    connected: NotRequired[bool]
    maxSamplingFrequency: NotRequired[float | None]
    minSamplingFrequency: NotRequired[float | None]

class MockSensor(TypedDict):
    maxSamplingFrequency: NotRequired[float]
    minSamplingFrequency: NotRequired[float]
    requestedSamplingFrequency: NotRequired[float]

class MockSensorReadingValues(TypedDict): ...

class GeolocationSensor(Sensor):
    @classmethod
    def new(self, options: GeolocationSensorOptions | None = {}) -> GeolocationSensor: ...
    latitude: float | None
    longitude: float | None
    altitude: float | None
    accuracy: float | None
    altitudeAccuracy: float | None
    heading: float | None
    speed: float | None

class GeolocationSensorOptions(TypedDict, SensorOptions): ...

class ReadOptions(TypedDict, GeolocationSensorOptions):
    signal: NotRequired[AbortSignal | None]

class GeolocationSensorReading(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp | None]
    latitude: NotRequired[float | None]
    longitude: NotRequired[float | None]
    altitude: NotRequired[float | None]
    accuracy: NotRequired[float | None]
    altitudeAccuracy: NotRequired[float | None]
    heading: NotRequired[float | None]
    speed: NotRequired[float | None]

class GeolocationReadingValues(TypedDict):
    latitude: float | None
    longitude: float | None
    altitude: float | None
    accuracy: float | None
    altitudeAccuracy: float | None
    heading: float | None
    speed: float | None

class Geolocation:
    def getCurrentPosition(self, successCallback: PositionCallback, errorCallback: PositionErrorCallback | None = None, options: PositionOptions | None = {}): ...
    def watchPosition(self, successCallback: PositionCallback, errorCallback: PositionErrorCallback | None = None, options: PositionOptions | None = {}) -> int: ...
    def clearWatch(self, watchId: int): ...

class PositionOptions(TypedDict):
    enableHighAccuracy: NotRequired[bool]
    timeout: NotRequired[int]
    maximumAge: NotRequired[int]

class GeolocationPosition:
    coords: GeolocationCoordinates
    timestamp: EpochTimeStamp

class GeolocationCoordinates:
    accuracy: float
    latitude: float
    longitude: float
    altitude: float | None
    altitudeAccuracy: float | None
    heading: float | None
    speed: float | None

class GeolocationPositionError:
    PERMISSION_DENIED = 1
    POSITION_UNAVAILABLE = 2
    TIMEOUT = 3
    code: int
    message: str

class DOMPointReadOnly:
    @classmethod
    def new(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, w: float | None = 1) -> DOMPointReadOnly: ...
    x: float
    y: float
    z: float
    w: float
    def matrixTransform(self, matrix: DOMMatrixInit | None = {}) -> DOMPoint: ...
    def toJSON(self) -> object: ...

class DOMPoint(DOMPointReadOnly):
    @classmethod
    def new(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, w: float | None = 1) -> DOMPoint: ...
    x: float
    y: float
    z: float
    w: float

class DOMPointInit(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]
    z: NotRequired[float]
    w: NotRequired[float]

class DOMRectReadOnly:
    @classmethod
    def new(self, x: float | None = 0, y: float | None = 0, width: float | None = 0, height: float | None = 0) -> DOMRectReadOnly: ...
    x: float
    y: float
    width: float
    height: float
    top: float
    right: float
    bottom: float
    left: float
    def toJSON(self) -> object: ...

class DOMRect(DOMRectReadOnly):
    @classmethod
    def new(self, x: float | None = 0, y: float | None = 0, width: float | None = 0, height: float | None = 0) -> DOMRect: ...
    x: float
    y: float
    width: float
    height: float

class DOMRectInit(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]
    width: NotRequired[float]
    height: NotRequired[float]

class DOMRectList:
    length: int

class DOMQuad:
    @classmethod
    def new(self, p1: DOMPointInit | None = {}, p2: DOMPointInit | None = {}, p3: DOMPointInit | None = {}, p4: DOMPointInit | None = {}) -> DOMQuad: ...
    p1: DOMPoint
    p2: DOMPoint
    p3: DOMPoint
    p4: DOMPoint
    def getBounds(self) -> DOMRect: ...
    def toJSON(self) -> object: ...

class DOMQuadInit(TypedDict):
    p1: NotRequired[DOMPointInit]
    p2: NotRequired[DOMPointInit]
    p3: NotRequired[DOMPointInit]
    p4: NotRequired[DOMPointInit]

class DOMMatrixReadOnly:
    @classmethod
    def new(self, init: str | Sequence[float] | None = None) -> DOMMatrixReadOnly: ...
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    m11: float
    m12: float
    m13: float
    m14: float
    m21: float
    m22: float
    m23: float
    m24: float
    m31: float
    m32: float
    m33: float
    m34: float
    m41: float
    m42: float
    m43: float
    m44: float
    is2D: bool
    isIdentity: bool
    def translate(self, tx: float | None = 0, ty: float | None = 0, tz: float | None = 0) -> DOMMatrix: ...
    def scale(self, scaleX: float | None = 1, scaleY: float | None = None, scaleZ: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def scaleNonUniform(self, scaleX: float | None = 1, scaleY: float | None = 1) -> DOMMatrix: ...
    def scale3d(self, scale: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def rotate(self, rotX: float | None = 0, rotY: float | None = None, rotZ: float | None = None) -> DOMMatrix: ...
    def rotateFromVector(self, x: float | None = 0, y: float | None = 0) -> DOMMatrix: ...
    def rotateAxisAngle(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, angle: float | None = 0) -> DOMMatrix: ...
    def skewX(self, sx: float | None = 0) -> DOMMatrix: ...
    def skewY(self, sy: float | None = 0) -> DOMMatrix: ...
    def multiply(self, other: DOMMatrixInit | None = {}) -> DOMMatrix: ...
    def flipX(self) -> DOMMatrix: ...
    def flipY(self) -> DOMMatrix: ...
    def inverse(self) -> DOMMatrix: ...
    def transformPoint(self, point: DOMPointInit | None = {}) -> DOMPoint: ...
    def toFloat32Array(self) -> Float32Array: ...
    def toFloat64Array(self) -> Float64Array: ...
    def toJSON(self) -> object: ...

class DOMMatrix(DOMMatrixReadOnly):
    @classmethod
    def new(self, init: str | Sequence[float] | None = None) -> DOMMatrix: ...
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    m11: float
    m12: float
    m13: float
    m14: float
    m21: float
    m22: float
    m23: float
    m24: float
    m31: float
    m32: float
    m33: float
    m34: float
    m41: float
    m42: float
    m43: float
    m44: float
    def multiplySelf(self, other: DOMMatrixInit | None = {}) -> DOMMatrix: ...
    def preMultiplySelf(self, other: DOMMatrixInit | None = {}) -> DOMMatrix: ...
    def translateSelf(self, tx: float | None = 0, ty: float | None = 0, tz: float | None = 0) -> DOMMatrix: ...
    def scaleSelf(self, scaleX: float | None = 1, scaleY: float | None = None, scaleZ: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def scale3dSelf(self, scale: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def rotateSelf(self, rotX: float | None = 0, rotY: float | None = None, rotZ: float | None = None) -> DOMMatrix: ...
    def rotateFromVectorSelf(self, x: float | None = 0, y: float | None = 0) -> DOMMatrix: ...
    def rotateAxisAngleSelf(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, angle: float | None = 0) -> DOMMatrix: ...
    def skewXSelf(self, sx: float | None = 0) -> DOMMatrix: ...
    def skewYSelf(self, sy: float | None = 0) -> DOMMatrix: ...
    def invertSelf(self) -> DOMMatrix: ...
    def setMatrixValue(self, transformList: str) -> DOMMatrix: ...

class DOMMatrix2DInit(TypedDict):
    a: NotRequired[float]
    b: NotRequired[float]
    c: NotRequired[float]
    d: NotRequired[float]
    e: NotRequired[float]
    f: NotRequired[float]
    m11: NotRequired[float]
    m12: NotRequired[float]
    m21: NotRequired[float]
    m22: NotRequired[float]
    m41: NotRequired[float]
    m42: NotRequired[float]

class DOMMatrixInit(TypedDict, DOMMatrix2DInit):
    m13: NotRequired[float]
    m14: NotRequired[float]
    m23: NotRequired[float]
    m24: NotRequired[float]
    m31: NotRequired[float]
    m32: NotRequired[float]
    m33: NotRequired[float]
    m34: NotRequired[float]
    m43: NotRequired[float]
    m44: NotRequired[float]
    is2D: NotRequired[bool]

class RelatedApplication(TypedDict):
    platform: USVString
    url: NotRequired[USVString]
    id: NotRequired[str]
    version: NotRequired[USVString]

class Gyroscope(Sensor):
    @classmethod
    def new(self, sensorOptions: GyroscopeSensorOptions | None = {}) -> Gyroscope: ...
    x: float | None
    y: float | None
    z: float | None

class GyroscopeSensorOptions(TypedDict, SensorOptions):
    referenceFrame: NotRequired[GyroscopeLocalCoordinateSystem]

class GyroscopeReadingValues(TypedDict):
    x: float | None
    y: float | None
    z: float | None

class HTMLAllCollection:
    length: int
    def item(self, nameOrIndex: str | None = None) -> HTMLCollection | Element | None: ...

class HTMLFormControlsCollection(HTMLCollection): ...

class RadioNodeList(NodeList):
    value: str

class HTMLOptionsCollection(HTMLCollection):
    length: int
    def add(self, element: HTMLOptionElement | HTMLOptGroupElement, before: HTMLElement | int | None = None): ...
    def remove(self, index: int): ...
    selectedIndex: int

class DOMStringList:
    length: int
    def contains(self, string: str) -> bool: ...

class HTMLUnknownElement(HTMLElement): ...

class HTMLOrSVGElement:
    dataset: DOMStringMap
    nonce: str
    autofocus: bool
    tabIndex: int
    def focus(self, options: FocusOptions | None = {}): ...
    def blur(self): ...

class DOMStringMap: ...

class HTMLHtmlElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLHtmlElement: ...
    version: str

class HTMLHeadElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLHeadElement: ...

class HTMLTitleElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTitleElement: ...
    text: str

class HTMLBaseElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLBaseElement: ...
    href: USVString
    target: str

class HTMLLinkElement(HTMLElement, LinkStyle):
    @classmethod
    def new(self) -> HTMLLinkElement: ...
    href: USVString
    crossOrigin: str | None
    rel: str
    relList: DOMTokenList
    media: str
    integrity: str
    hreflang: str
    type: str
    sizes: DOMTokenList
    imageSrcset: USVString
    imageSizes: str
    referrerPolicy: str
    blocking: DOMTokenList
    disabled: bool
    charset: str
    rev: str
    target: str
    fetchPriority: str

class HTMLMetaElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLMetaElement: ...
    name: str
    httpEquiv: str
    content: str
    media: str
    scheme: str

class HTMLStyleElement(HTMLElement, LinkStyle):
    @classmethod
    def new(self) -> HTMLStyleElement: ...
    disabled: bool
    media: str
    blocking: DOMTokenList
    type: str

class HTMLHeadingElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLHeadingElement: ...
    align: str

class HTMLParagraphElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLParagraphElement: ...
    align: str

class HTMLHRElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLHRElement: ...
    align: str
    color: str
    noShade: bool
    size: str
    width: str

class HTMLPreElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLPreElement: ...
    width: int

class HTMLQuoteElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLQuoteElement: ...
    cite: USVString

class HTMLOListElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLOListElement: ...
    reversed: bool
    start: int
    type: str
    compact: bool

class HTMLUListElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLUListElement: ...
    compact: bool
    type: str

class HTMLMenuElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLMenuElement: ...
    compact: bool

class HTMLLIElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLLIElement: ...
    value: int
    type: str

class HTMLDListElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDListElement: ...
    compact: bool

class HTMLDivElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDivElement: ...
    align: str

class HTMLDataElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDataElement: ...
    value: str

class HTMLTimeElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTimeElement: ...
    dateTime: str

class HTMLSpanElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLSpanElement: ...

class HTMLBRElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLBRElement: ...
    clear: str

class HTMLHyperlinkElementUtils:
    href: USVString
    origin: USVString
    protocol: USVString
    username: USVString
    password: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class HTMLModElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLModElement: ...
    cite: USVString
    dateTime: str

class HTMLPictureElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLPictureElement: ...

class HTMLSourceElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLSourceElement: ...
    src: USVString
    type: str
    srcset: USVString
    sizes: str
    media: str
    width: int
    height: int

class HTMLEmbedElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLEmbedElement: ...
    src: USVString
    type: str
    width: str
    height: str
    def getSVGDocument(self) -> Document | None: ...
    align: str
    name: str

class HTMLObjectElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLObjectElement: ...
    data: USVString
    type: str
    name: str
    form: HTMLFormElement | None
    width: str
    height: str
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    def getSVGDocument(self) -> Document | None: ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    align: str
    archive: str
    code: str
    declare: bool
    hspace: int
    standby: str
    vspace: int
    codeBase: str
    codeType: str
    useMap: str
    border: str

class HTMLVideoElement(HTMLMediaElement):
    @classmethod
    def new(self) -> HTMLVideoElement: ...
    width: int
    height: int
    videoWidth: int
    videoHeight: int
    poster: USVString
    playsInline: bool
    def getVideoPlaybackQuality(self) -> VideoPlaybackQuality: ...
    def requestPictureInPicture(self) -> Awaitable[PictureInPictureWindow]: ...
    onenterpictureinpicture: EventHandler
    onleavepictureinpicture: EventHandler
    disablePictureInPicture: bool
    def requestVideoFrameCallback(self, callback: VideoFrameRequestCallback) -> int: ...
    def cancelVideoFrameCallback(self, handle: int): ...

class HTMLAudioElement(HTMLMediaElement):
    @classmethod
    def new(self) -> HTMLAudioElement: ...
    """ # GIgnoredStmt 
    LegacyFactoryFunction=Audio(optional DOMString src)
    """

class HTMLTrackElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTrackElement: ...
    kind: str
    src: USVString
    srclang: str
    label: str
    default: bool
    NONE = 0
    LOADING = 1
    LOADED = 2
    ERROR = 3
    readyState: int
    track: TextTrack

class MediaError:
    MEDIA_ERR_ABORTED = 1
    MEDIA_ERR_NETWORK = 2
    MEDIA_ERR_DECODE = 3
    MEDIA_ERR_SRC_NOT_SUPPORTED = 4
    code: int
    message: str

class AudioTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> AudioTrack | None: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class AudioTrack:
    id: str
    kind: str
    label: str
    language: str
    enabled: bool
    sourceBuffer: SourceBuffer | None

class VideoTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> VideoTrack | None: ...
    selectedIndex: int
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class VideoTrack:
    id: str
    kind: str
    label: str
    language: str
    selected: bool
    sourceBuffer: SourceBuffer | None

class TextTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> TextTrack | None: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class TextTrack(EventTarget):
    kind: TextTrackKind
    label: str
    language: str
    id: str
    inBandMetadataTrackDispatchType: str
    mode: TextTrackMode
    cues: TextTrackCueList | None
    activeCues: TextTrackCueList | None
    def addCue(self, cue: TextTrackCue): ...
    def removeCue(self, cue: TextTrackCue): ...
    oncuechange: EventHandler
    sourceBuffer: SourceBuffer | None

class TextTrackCueList:
    length: int
    def getCueById(self, id: str) -> TextTrackCue | None: ...

class TextTrackCue(EventTarget):
    track: TextTrack | None
    id: str
    startTime: float
    endTime: float
    pauseOnExit: bool
    onenter: EventHandler
    onexit: EventHandler

class TimeRanges:
    length: int
    def start(self, index: int) -> float: ...
    def end(self, index: int) -> float: ...

class TrackEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: TrackEventInit | None = {}) -> TrackEvent: ...
    track: VideoTrack | AudioTrack | TextTrack | None

class TrackEventInit(TypedDict, EventInit):
    track: NotRequired[VideoTrack | AudioTrack | TextTrack | None]

class HTMLMapElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLMapElement: ...
    name: str
    areas: HTMLCollection

class HTMLAreaElement(HTMLElement, HTMLHyperlinkElementUtils):
    @classmethod
    def new(self) -> HTMLAreaElement: ...
    alt: str
    coords: str
    shape: str
    target: str
    download: str
    ping: USVString
    rel: str
    relList: DOMTokenList
    referrerPolicy: str
    noHref: bool

class HTMLTableElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTableElement: ...
    caption: HTMLTableCaptionElement | None
    def createCaption(self) -> HTMLTableCaptionElement: ...
    def deleteCaption(self): ...
    tHead: HTMLTableSectionElement | None
    def createTHead(self) -> HTMLTableSectionElement: ...
    def deleteTHead(self): ...
    tFoot: HTMLTableSectionElement | None
    def createTFoot(self) -> HTMLTableSectionElement: ...
    def deleteTFoot(self): ...
    tBodies: HTMLCollection
    def createTBody(self) -> HTMLTableSectionElement: ...
    rows: HTMLCollection
    def insertRow(self, index: int | None = -1) -> HTMLTableRowElement: ...
    def deleteRow(self, index: int): ...
    align: str
    border: str
    frame: str
    rules: str
    summary: str
    width: str
    bgColor: str
    cellPadding: str
    cellSpacing: str

class HTMLTableCaptionElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTableCaptionElement: ...
    align: str

class HTMLTableColElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTableColElement: ...
    span: int
    align: str
    ch: str
    chOff: str
    vAlign: str
    width: str

class HTMLTableSectionElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTableSectionElement: ...
    rows: HTMLCollection
    def insertRow(self, index: int | None = -1) -> HTMLTableRowElement: ...
    def deleteRow(self, index: int): ...
    align: str
    ch: str
    chOff: str
    vAlign: str

class HTMLTableRowElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTableRowElement: ...
    rowIndex: int
    sectionRowIndex: int
    cells: HTMLCollection
    def insertCell(self, index: int | None = -1) -> HTMLTableCellElement: ...
    def deleteCell(self, index: int): ...
    align: str
    ch: str
    chOff: str
    vAlign: str
    bgColor: str

class HTMLTableCellElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTableCellElement: ...
    colSpan: int
    rowSpan: int
    headers: str
    cellIndex: int
    scope: str
    abbr: str
    align: str
    axis: str
    height: str
    width: str
    ch: str
    chOff: str
    noWrap: bool
    vAlign: str
    bgColor: str

class HTMLFormElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLFormElement: ...
    acceptCharset: str
    action: USVString
    autocomplete: str
    enctype: str
    encoding: str
    method: str
    name: str
    noValidate: bool
    target: str
    rel: str
    relList: DOMTokenList
    elements: HTMLFormControlsCollection
    length: int
    def submit(self): ...
    def requestSubmit(self, submitter: HTMLElement | None = None): ...
    def reset(self): ...
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...

class HTMLLabelElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLLabelElement: ...
    form: HTMLFormElement | None
    htmlFor: str
    control: HTMLElement | None

class HTMLButtonElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLButtonElement: ...
    disabled: bool
    form: HTMLFormElement | None
    formAction: USVString
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    name: str
    type: str
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList

class HTMLSelectElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLSelectElement: ...
    autocomplete: str
    disabled: bool
    form: HTMLFormElement | None
    multiple: bool
    name: str
    required: bool
    size: int
    type: str
    options: HTMLOptionsCollection
    length: int
    def namedItem(self, name: str) -> HTMLOptionElement | None: ...
    def add(self, element: HTMLOptionElement | HTMLOptGroupElement, before: HTMLElement | int | None = None): ...
    @overload
    def remove(self): ...
    @overload
    def remove(self, index: int): ...
    selectedOptions: HTMLCollection
    selectedIndex: int
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList

class HTMLDataListElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDataListElement: ...
    options: HTMLCollection

class HTMLOptGroupElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLOptGroupElement: ...
    disabled: bool
    label: str

class HTMLOptionElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLOptionElement: ...
    """ # GIgnoredStmt 
    LegacyFactoryFunction=Option(optional DOMString text = "", optional DOMString value, optional boolean defaultSelected = false, optional boolean selected = false)
    """
    disabled: bool
    form: HTMLFormElement | None
    label: str
    defaultSelected: bool
    selected: bool
    value: str
    text: str
    index: int

class HTMLTextAreaElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTextAreaElement: ...
    autocomplete: str
    cols: int
    dirName: str
    disabled: bool
    form: HTMLFormElement | None
    maxLength: int
    minLength: int
    name: str
    placeholder: str
    readOnly: bool
    required: bool
    rows: int
    wrap: str
    type: str
    defaultValue: str
    value: str
    textLength: int
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList
    def select(self): ...
    selectionStart: int
    selectionEnd: int
    selectionDirection: str
    @overload
    def setRangeText(self, replacement: str): ...
    @overload
    def setRangeText(self, replacement: str, start: int, end: int, selectionMode: SelectionMode | None = "preserve"): ...
    def setSelectionRange(self, start: int, end: int, direction: str | None = None): ...

class HTMLOutputElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLOutputElement: ...
    htmlFor: DOMTokenList
    form: HTMLFormElement | None
    name: str
    type: str
    defaultValue: str
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList

class HTMLProgressElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLProgressElement: ...
    value: float
    max: float
    position: float
    labels: NodeList

class HTMLMeterElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLMeterElement: ...
    value: float
    min: float
    max: float
    low: float
    high: float
    optimum: float
    labels: NodeList

class HTMLFieldSetElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLFieldSetElement: ...
    disabled: bool
    form: HTMLFormElement | None
    name: str
    type: str
    elements: HTMLCollection
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...

class HTMLLegendElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLLegendElement: ...
    form: HTMLFormElement | None
    align: str

class ValidityState:
    valueMissing: bool
    typeMismatch: bool
    patternMismatch: bool
    tooLong: bool
    tooShort: bool
    rangeUnderflow: bool
    rangeOverflow: bool
    stepMismatch: bool
    badInput: bool
    customError: bool
    valid: bool

class SubmitEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: SubmitEventInit | None = {}) -> SubmitEvent: ...
    submitter: HTMLElement | None

class SubmitEventInit(TypedDict, EventInit):
    submitter: NotRequired[HTMLElement | None]

class FormDataEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: FormDataEventInit) -> FormDataEvent: ...
    formData: FormData

class FormDataEventInit(TypedDict, EventInit):
    formData: FormData

class HTMLDetailsElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDetailsElement: ...
    open: bool

class HTMLDialogElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDialogElement: ...
    open: bool
    returnValue: str
    def show(self): ...
    def showModal(self): ...
    def close(self, returnValue: str | None = None): ...

class HTMLTemplateElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLTemplateElement: ...
    content: DocumentFragment

class HTMLSlotElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLSlotElement: ...
    name: str
    def assignedNodes(self, options: AssignedNodesOptions | None = {}) -> Sequence[Node]: ...
    def assignedElements(self, options: AssignedNodesOptions | None = {}) -> Sequence[Element]: ...
    def assign(self, *nodes: Element | Text): ...

class AssignedNodesOptions(TypedDict):
    flatten: NotRequired[bool]

class HTMLCanvasElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLCanvasElement: ...
    width: int
    height: int
    def getContext(self, contextId: str, options: Any | None = None) -> RenderingContext | None: ...
    def toDataURL(self, type: str | None = "image/png", quality: Any | None = None) -> USVString: ...
    def toBlob(self, callback: BlobCallback, type: str | None = "image/png", quality: Any | None = None): ...
    def transferControlToOffscreen(self) -> OffscreenCanvas: ...
    def captureStream(self, frameRequestRate: float | None = None) -> MediaStream: ...

class CanvasRenderingContext2DSettings(TypedDict):
    alpha: NotRequired[bool]
    desynchronized: NotRequired[bool]
    colorSpace: NotRequired[PredefinedColorSpace]
    willReadFrequently: NotRequired[bool]

class CanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath, CanvasUserInterface, CanvasText, CanvasDrawImage, CanvasImageData, CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPath):
    canvas: HTMLCanvasElement
    def getContextAttributes(self) -> CanvasRenderingContext2DSettings: ...

class CanvasState:
    def save(self): ...
    def restore(self): ...
    def reset(self): ...
    def isContextLost(self) -> bool: ...

class CanvasTransform:
    def scale(self, x: float, y: float): ...
    def rotate(self, angle: float): ...
    def translate(self, x: float, y: float): ...
    def transform(self, a: float, b: float, c: float, d: float, e: float, f: float): ...
    def getTransform(self) -> DOMMatrix: ...
    @overload
    def setTransform(self, a: float, b: float, c: float, d: float, e: float, f: float): ...
    @overload
    def setTransform(self, transform: DOMMatrix2DInit | None = {}): ...
    def resetTransform(self): ...

class CanvasCompositing:
    globalAlpha: float
    globalCompositeOperation: str

class CanvasImageSmoothing:
    imageSmoothingEnabled: bool
    imageSmoothingQuality: ImageSmoothingQuality

class CanvasFillStrokeStyles:
    strokeStyle: str | CanvasGradient | CanvasPattern
    fillStyle: str | CanvasGradient | CanvasPattern
    def createLinearGradient(self, x0: float, y0: float, x1: float, y1: float) -> CanvasGradient: ...
    def createRadialGradient(self, x0: float, y0: float, r0: float, x1: float, y1: float, r1: float) -> CanvasGradient: ...
    def createConicGradient(self, startAngle: float, x: float, y: float) -> CanvasGradient: ...
    def createPattern(self, image: CanvasImageSource, repetition: str) -> CanvasPattern | None: ...

class CanvasShadowStyles:
    shadowOffsetX: float
    shadowOffsetY: float
    shadowBlur: float
    shadowColor: str

class CanvasFilters:
    filter: str

class CanvasRect:
    def clearRect(self, x: float, y: float, w: float, h: float): ...
    def fillRect(self, x: float, y: float, w: float, h: float): ...
    def strokeRect(self, x: float, y: float, w: float, h: float): ...

class CanvasDrawPath:
    def beginPath(self): ...
    @overload
    def fill(self, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def fill(self, path: Path2D, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def stroke(self): ...
    @overload
    def stroke(self, path: Path2D): ...
    @overload
    def clip(self, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def clip(self, path: Path2D, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def isPointInPath(self, x: float, y: float, fillRule: CanvasFillRule | None = "nonzero") -> bool: ...
    @overload
    def isPointInPath(self, path: Path2D, x: float, y: float, fillRule: CanvasFillRule | None = "nonzero") -> bool: ...
    @overload
    def isPointInStroke(self, x: float, y: float) -> bool: ...
    @overload
    def isPointInStroke(self, path: Path2D, x: float, y: float) -> bool: ...

class CanvasUserInterface:
    @overload
    def drawFocusIfNeeded(self, element: Element): ...
    @overload
    def drawFocusIfNeeded(self, path: Path2D, element: Element): ...
    @overload
    def scrollPathIntoView(self): ...
    @overload
    def scrollPathIntoView(self, path: Path2D): ...

class CanvasText:
    def fillText(self, text: str, x: float, y: float, maxWidth: float | None = None): ...
    def strokeText(self, text: str, x: float, y: float, maxWidth: float | None = None): ...
    def measureText(self, text: str) -> TextMetrics: ...

class CanvasDrawImage:
    @overload
    def drawImage(self, image: CanvasImageSource, dx: float, dy: float): ...
    @overload
    def drawImage(self, image: CanvasImageSource, dx: float, dy: float, dw: float, dh: float): ...
    @overload
    def drawImage(self, image: CanvasImageSource, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float, dh: float): ...

class CanvasImageData:
    @overload
    def createImageData(self, sw: int, sh: int, settings: ImageDataSettings | None = {}) -> ImageData: ...
    @overload
    def createImageData(self, imagedata: ImageData) -> ImageData: ...
    def getImageData(self, sx: int, sy: int, sw: int, sh: int, settings: ImageDataSettings | None = {}) -> ImageData: ...
    @overload
    def putImageData(self, imagedata: ImageData, dx: int, dy: int): ...
    @overload
    def putImageData(self, imagedata: ImageData, dx: int, dy: int, dirtyX: int, dirtyY: int, dirtyWidth: int, dirtyHeight: int): ...

class CanvasPathDrawingStyles:
    lineWidth: float
    lineCap: CanvasLineCap
    lineJoin: CanvasLineJoin
    miterLimit: float
    def setLineDash(self, segments: Sequence[float]): ...
    def getLineDash(self) -> Sequence[float]: ...
    lineDashOffset: float

class CanvasTextDrawingStyles:
    font: str
    textAlign: CanvasTextAlign
    textBaseline: CanvasTextBaseline
    direction: CanvasDirection
    letterSpacing: str
    fontKerning: CanvasFontKerning
    fontStretch: CanvasFontStretch
    fontVariantCaps: CanvasFontVariantCaps
    textRendering: CanvasTextRendering
    wordSpacing: str

class CanvasPath:
    def closePath(self): ...
    def moveTo(self, x: float, y: float): ...
    def lineTo(self, x: float, y: float): ...
    def quadraticCurveTo(self, cpx: float, cpy: float, x: float, y: float): ...
    def bezierCurveTo(self, cp1x: float, cp1y: float, cp2x: float, cp2y: float, x: float, y: float): ...
    def arcTo(self, x1: float, y1: float, x2: float, y2: float, radius: float): ...
    def rect(self, x: float, y: float, w: float, h: float): ...
    def roundRect(self, x: float, y: float, w: float, h: float, radii: float | DOMPointInit | Sequence[float | DOMPointInit] | None = 0): ...
    def arc(self, x: float, y: float, radius: float, startAngle: float, endAngle: float, counterclockwise: bool | None = false): ...
    def ellipse(self, x: float, y: float, radiusX: float, radiusY: float, rotation: float, startAngle: float, endAngle: float, counterclockwise: bool | None = false): ...

class CanvasGradient:
    def addColorStop(self, offset: float, color: str): ...

class CanvasPattern:
    def setTransform(self, transform: DOMMatrix2DInit | None = {}): ...

class TextMetrics:
    width: float
    actualBoundingBoxLeft: float
    actualBoundingBoxRight: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    actualBoundingBoxAscent: float
    actualBoundingBoxDescent: float
    emHeightAscent: float
    emHeightDescent: float
    hangingBaseline: float
    alphabeticBaseline: float
    ideographicBaseline: float

class ImageDataSettings(TypedDict):
    colorSpace: NotRequired[PredefinedColorSpace]

class ImageData:
    @overload
    @classmethod
    def new(self, sw: int, sh: int, settings: ImageDataSettings | None = {}) -> ImageData: ...
    @overload
    @classmethod
    def new(self, data: Uint8ClampedArray, sw: int, sh: int | None = None, settings: ImageDataSettings | None = {}) -> ImageData: ...
    width: int
    height: int
    data: Uint8ClampedArray
    colorSpace: PredefinedColorSpace

class Path2D(CanvasPath):
    @classmethod
    def new(self, path: Path2D | str | None = None) -> Path2D: ...
    def addPath(self, path: Path2D, transform: DOMMatrix2DInit | None = {}): ...

class ImageBitmapRenderingContext:
    canvas: HTMLCanvasElement | OffscreenCanvas
    def transferFromImageBitmap(self, bitmap: ImageBitmap | None): ...

class ImageBitmapRenderingContextSettings(TypedDict):
    alpha: NotRequired[bool]

class ImageEncodeOptions(TypedDict):
    type: NotRequired[str]
    quality: NotRequired[float]

class OffscreenCanvas(EventTarget):
    @classmethod
    def new(self, width: int, height: int) -> OffscreenCanvas: ...
    width: int
    height: int
    def getContext(self, contextId: OffscreenRenderingContextId, options: Any | None = None) -> OffscreenRenderingContext | None: ...
    def transferToImageBitmap(self) -> ImageBitmap: ...
    def convertToBlob(self, options: ImageEncodeOptions | None = {}) -> Awaitable[Blob]: ...
    oncontextlost: EventHandler
    oncontextrestored: EventHandler

class OffscreenCanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath, CanvasText, CanvasDrawImage, CanvasImageData, CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPath):
    def commit(self): ...
    canvas: OffscreenCanvas

class CustomElementRegistry:
    def define(self, name: str, constructor: CustomElementConstructor, options: ElementDefinitionOptions | None = {}): ...
    def get(self, name: str) -> CustomElementConstructor | None: ...
    def whenDefined(self, name: str) -> Awaitable[CustomElementConstructor]: ...
    def upgrade(self, root: Node): ...

class ElementDefinitionOptions(TypedDict):
    extends: NotRequired[str]

class ValidityStateFlags(TypedDict):
    valueMissing: NotRequired[bool]
    typeMismatch: NotRequired[bool]
    patternMismatch: NotRequired[bool]
    tooLong: NotRequired[bool]
    tooShort: NotRequired[bool]
    rangeUnderflow: NotRequired[bool]
    rangeOverflow: NotRequired[bool]
    stepMismatch: NotRequired[bool]
    badInput: NotRequired[bool]
    customError: NotRequired[bool]

class UserActivation:
    hasBeenActive: bool
    isActive: bool

class FocusOptions(TypedDict):
    preventScroll: NotRequired[bool]
    focusVisible: NotRequired[bool]

class ElementContentEditable:
    contentEditable: str
    enterKeyHint: str
    isContentEditable: bool
    inputMode: str
    virtualKeyboardPolicy: str

class DataTransfer:
    @classmethod
    def new(self) -> DataTransfer: ...
    dropEffect: str
    effectAllowed: str
    items: DataTransferItemList
    def setDragImage(self, image: Element, x: int, y: int): ...
    types: Sequence[str]
    def getData(self, format: str) -> str: ...
    def setData(self, format: str, data: str): ...
    def clearData(self, format: str | None = None): ...
    files: FileList

class DataTransferItemList:
    length: int
    @overload
    def add(self, data: str, type: str) -> DataTransferItem | None: ...
    @overload
    def add(self, data: File) -> DataTransferItem | None: ...
    def remove(self, index: int): ...
    def clear(self): ...

class DragEvent(MouseEvent):
    @classmethod
    def new(self, type: str, eventInitDict: DragEventInit | None = {}) -> DragEvent: ...
    dataTransfer: DataTransfer | None

class DragEventInit(TypedDict, MouseEventInit):
    dataTransfer: NotRequired[DataTransfer | None]

class WindowPostMessageOptions(TypedDict, StructuredSerializeOptions):
    targetOrigin: NotRequired[USVString]

class BarProp:
    visible: bool

class Location:
    href: USVString
    origin: USVString
    protocol: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString
    def assign(self, url: USVString): ...
    def replace(self, url: USVString): ...
    def reload(self): ...
    ancestorOrigins: DOMStringList

class History:
    length: int
    scrollRestoration: ScrollRestoration
    state: Any
    def go(self, delta: int | None = 0): ...
    def back(self): ...
    def forward(self): ...
    def pushState(self, data: Any, unused: str, url: USVString | None = None): ...
    def replaceState(self, data: Any, unused: str, url: USVString | None = None): ...

class PopStateEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PopStateEventInit | None = {}) -> PopStateEvent: ...
    state: Any

class PopStateEventInit(TypedDict, EventInit):
    state: NotRequired[Any]

class HashChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: HashChangeEventInit | None = {}) -> HashChangeEvent: ...
    oldURL: USVString
    newURL: USVString

class HashChangeEventInit(TypedDict, EventInit):
    oldURL: NotRequired[USVString]
    newURL: NotRequired[USVString]

class PageTransitionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PageTransitionEventInit | None = {}) -> PageTransitionEvent: ...
    persisted: bool

class PageTransitionEventInit(TypedDict, EventInit):
    persisted: NotRequired[bool]

class BeforeUnloadEvent(Event):
    returnValue: str

class ErrorEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: ErrorEventInit | None = {}) -> ErrorEvent: ...
    message: str
    filename: USVString
    lineno: int
    colno: int
    error: Any

class ErrorEventInit(TypedDict, EventInit):
    message: NotRequired[str]
    filename: NotRequired[USVString]
    lineno: NotRequired[int]
    colno: NotRequired[int]
    error: NotRequired[Any]

class PromiseRejectionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PromiseRejectionEventInit) -> PromiseRejectionEvent: ...
    promise: Awaitable[Any]
    reason: Any

class PromiseRejectionEventInit(TypedDict, EventInit):
    promise: Awaitable[Any]
    reason: NotRequired[Any]

class DOMParser:
    @classmethod
    def new(self) -> DOMParser: ...
    def parseFromString(self, string: str, type: DOMParserSupportedType) -> Document: ...

class NavigatorID:
    appCodeName: str
    appName: str
    appVersion: str
    platform: str
    product: str
    productSub: str
    userAgent: str
    vendor: str
    vendorSub: str
    def taintEnabled(self) -> bool: ...
    oscpu: str

class NavigatorLanguage:
    language: str
    languages: Sequence[str]

class NavigatorOnLine:
    onLine: bool

class NavigatorContentUtils:
    def registerProtocolHandler(self, scheme: str, url: USVString): ...
    def unregisterProtocolHandler(self, scheme: str, url: USVString): ...

class NavigatorCookies:
    cookieEnabled: bool

class NavigatorPlugins:
    plugins: PluginArray
    mimeTypes: MimeTypeArray
    def javaEnabled(self) -> bool: ...
    pdfViewerEnabled: bool

class PluginArray:
    def refresh(self): ...
    length: int

class MimeTypeArray:
    length: int

class Plugin:
    name: str
    description: str
    filename: str
    length: int

class MimeType:
    type: str
    description: str
    suffixes: str
    enabledPlugin: Plugin

class ImageBitmap:
    width: int
    height: int
    def close(self): ...

class ImageBitmapOptions(TypedDict):
    imageOrientation: NotRequired[ImageOrientation]
    premultiplyAlpha: NotRequired[PremultiplyAlpha]
    colorSpaceConversion: NotRequired[ColorSpaceConversion]
    resizeWidth: NotRequired[int]
    resizeHeight: NotRequired[int]
    resizeQuality: NotRequired[ResizeQuality]

class AnimationFrameProvider:
    def requestAnimationFrame(self, callback: FrameRequestCallback) -> int: ...
    def cancelAnimationFrame(self, handle: int): ...

class DedicatedWorkerGlobalScope(WorkerGlobalScope, AnimationFrameProvider):
    name: str
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]): ...
    @overload
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler
    onrtctransform: EventHandler

class MessageEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: MessageEventInit | None = {}) -> MessageEvent: ...
    data: Any
    origin: USVString
    lastEventId: str
    source: MessageEventSource | None
    ports: Sequence[MessagePort]
    def initMessageEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false, data: Any | None = None, origin: USVString | None = "", lastEventId: str | None = "", source: MessageEventSource | None = None, ports: Sequence[MessagePort] | None = []): ...

class MessageEventInit(TypedDict, EventInit):
    data: NotRequired[Any]
    origin: NotRequired[USVString]
    lastEventId: NotRequired[str]
    source: NotRequired[MessageEventSource | None]
    ports: NotRequired[Sequence[MessagePort]]

class EventSource(EventTarget):
    @classmethod
    def new(self, url: USVString, eventSourceInitDict: EventSourceInit | None = {}) -> EventSource: ...
    url: USVString
    withCredentials: bool
    CONNECTING = 0
    OPEN = 1
    CLOSED = 2
    readyState: int
    onopen: EventHandler
    onmessage: EventHandler
    onerror: EventHandler
    def close(self): ...

class EventSourceInit(TypedDict):
    withCredentials: NotRequired[bool]

class MessageChannel:
    @classmethod
    def new(self) -> MessageChannel: ...
    port1: MessagePort
    port2: MessagePort

class MessagePort(EventTarget):
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]): ...
    @overload
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...
    def start(self): ...
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class StructuredSerializeOptions(TypedDict):
    transfer: NotRequired[Sequence[object]]

class BroadcastChannel(EventTarget):
    @classmethod
    def new(self, name: str) -> BroadcastChannel: ...
    name: str
    def postMessage(self, message: Any): ...
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class SharedWorkerGlobalScope(WorkerGlobalScope):
    name: str
    def close(self): ...
    onconnect: EventHandler

class AbstractWorker:
    onerror: EventHandler

class Worker(EventTarget, AbstractWorker):
    @classmethod
    def new(self, scriptURL: USVString, options: WorkerOptions | None = {}) -> Worker: ...
    def terminate(self): ...
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]): ...
    @overload
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class WorkerOptions(TypedDict):
    type: NotRequired[WorkerType]
    credentials: NotRequired[RequestCredentials]
    name: NotRequired[str]

class SharedWorker(EventTarget, AbstractWorker):
    @classmethod
    def new(self, scriptURL: USVString, options: str | WorkerOptions | None = {}) -> SharedWorker: ...
    port: MessagePort

class NavigatorConcurrentHardware:
    hardwareConcurrency: int

class WorkerLocation:
    href: USVString
    origin: USVString
    protocol: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class WorkletGlobalScope: ...

class Worklet:
    def addModule(self, moduleURL: USVString, options: WorkletOptions | None = {}) -> Awaitable[None]: ...

class WorkletOptions(TypedDict):
    credentials: NotRequired[RequestCredentials]

class Storage:
    length: int
    def key(self, index: int) -> str | None: ...
    def clear(self): ...

class WindowSessionStorage:
    sessionStorage: Storage

class WindowLocalStorage:
    localStorage: Storage

class StorageEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: StorageEventInit | None = {}) -> StorageEvent: ...
    key: str | None
    oldValue: str | None
    newValue: str | None
    url: USVString
    storageArea: Storage | None
    def initStorageEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false, key: str | None = None, oldValue: str | None = None, newValue: str | None = None, url: USVString | None = "", storageArea: Storage | None = None): ...

class StorageEventInit(TypedDict, EventInit):
    key: NotRequired[str | None]
    oldValue: NotRequired[str | None]
    newValue: NotRequired[str | None]
    url: NotRequired[USVString]
    storageArea: NotRequired[Storage | None]

class HTMLMarqueeElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLMarqueeElement: ...
    behavior: str
    bgColor: str
    direction: str
    height: str
    hspace: int
    loop: int
    scrollAmount: int
    scrollDelay: int
    trueSpeed: bool
    vspace: int
    width: str
    def start(self): ...
    def stop(self): ...

class HTMLFrameSetElement(HTMLElement, WindowEventHandlers):
    @classmethod
    def new(self) -> HTMLFrameSetElement: ...
    cols: str
    rows: str

class HTMLFrameElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLFrameElement: ...
    name: str
    scrolling: str
    src: USVString
    frameBorder: str
    longDesc: USVString
    noResize: bool
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    marginHeight: str
    marginWidth: str

class HTMLDirectoryElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLDirectoryElement: ...
    compact: bool

class HTMLFontElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLFontElement: ...
    color: str
    face: str
    size: str

class HTMLParamElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLParamElement: ...
    name: str
    value: str
    type: str
    valueType: str

class External:
    def AddSearchProvider(self): ...
    def IsSearchProviderInstalled(self): ...

class IdleOptions(TypedDict):
    threshold: NotRequired[int]
    signal: NotRequired[AbortSignal]

class IdleDetector(EventTarget):
    @classmethod
    def new(self) -> IdleDetector: ...
    userState: UserIdleState | None
    screenState: ScreenIdleState | None
    onchange: EventHandler
    def start(self, options: IdleOptions | None = {}) -> Awaitable[None]: ...

class ImageCapture:
    @classmethod
    def new(self, videoTrack: MediaStreamTrack) -> ImageCapture: ...
    def takePhoto(self, photoSettings: PhotoSettings | None = {}) -> Awaitable[Blob]: ...
    def getPhotoCapabilities(self) -> Awaitable[PhotoCapabilities]: ...
    def getPhotoSettings(self) -> Awaitable[PhotoSettings]: ...
    def grabFrame(self) -> Awaitable[ImageBitmap]: ...
    track: MediaStreamTrack

class PhotoCapabilities(TypedDict):
    redEyeReduction: NotRequired[RedEyeReduction]
    imageHeight: NotRequired[MediaSettingsRange]
    imageWidth: NotRequired[MediaSettingsRange]
    fillLightMode: NotRequired[Sequence[FillLightMode]]

class PhotoSettings(TypedDict):
    fillLightMode: NotRequired[FillLightMode]
    imageHeight: NotRequired[float]
    imageWidth: NotRequired[float]
    redEyeReduction: NotRequired[bool]

class MediaSettingsRange(TypedDict):
    max: NotRequired[float]
    min: NotRequired[float]
    step: NotRequired[float]

class MediaTrackSupportedConstraints(TypedDict, TypedDict, TypedDict):
    whiteBalanceMode: NotRequired[bool]
    exposureMode: NotRequired[bool]
    focusMode: NotRequired[bool]
    pointsOfInterest: NotRequired[bool]
    exposureCompensation: NotRequired[bool]
    exposureTime: NotRequired[bool]
    colorTemperature: NotRequired[bool]
    iso: NotRequired[bool]
    brightness: NotRequired[bool]
    contrast: NotRequired[bool]
    pan: NotRequired[bool]
    saturation: NotRequired[bool]
    sharpness: NotRequired[bool]
    focusDistance: NotRequired[bool]
    tilt: NotRequired[bool]
    zoom: NotRequired[bool]
    torch: NotRequired[bool]
    width: NotRequired[bool]
    height: NotRequired[bool]
    aspectRatio: NotRequired[bool]
    frameRate: NotRequired[bool]
    facingMode: NotRequired[bool]
    resizeMode: NotRequired[bool]
    sampleRate: NotRequired[bool]
    sampleSize: NotRequired[bool]
    echoCancellation: NotRequired[bool]
    autoGainControl: NotRequired[bool]
    noiseSuppression: NotRequired[bool]
    latency: NotRequired[bool]
    channelCount: NotRequired[bool]
    deviceId: NotRequired[bool]
    groupId: NotRequired[bool]
    displaySurface: NotRequired[bool]
    logicalSurface: NotRequired[bool]
    cursor: NotRequired[bool]
    restrictOwnAudio: NotRequired[bool]
    suppressLocalAudioPlayback: NotRequired[bool]

class MediaTrackCapabilities(TypedDict, TypedDict, TypedDict):
    whiteBalanceMode: NotRequired[Sequence[str]]
    exposureMode: NotRequired[Sequence[str]]
    focusMode: NotRequired[Sequence[str]]
    exposureCompensation: NotRequired[MediaSettingsRange]
    exposureTime: NotRequired[MediaSettingsRange]
    colorTemperature: NotRequired[MediaSettingsRange]
    iso: NotRequired[MediaSettingsRange]
    brightness: NotRequired[MediaSettingsRange]
    contrast: NotRequired[MediaSettingsRange]
    saturation: NotRequired[MediaSettingsRange]
    sharpness: NotRequired[MediaSettingsRange]
    focusDistance: NotRequired[MediaSettingsRange]
    pan: NotRequired[MediaSettingsRange]
    tilt: NotRequired[MediaSettingsRange]
    zoom: NotRequired[MediaSettingsRange]
    torch: NotRequired[bool]
    width: NotRequired[ULongRange]
    height: NotRequired[ULongRange]
    aspectRatio: NotRequired[DoubleRange]
    frameRate: NotRequired[DoubleRange]
    facingMode: NotRequired[Sequence[str]]
    resizeMode: NotRequired[Sequence[str]]
    sampleRate: NotRequired[ULongRange]
    sampleSize: NotRequired[ULongRange]
    echoCancellation: NotRequired[Sequence[bool]]
    autoGainControl: NotRequired[Sequence[bool]]
    noiseSuppression: NotRequired[Sequence[bool]]
    latency: NotRequired[DoubleRange]
    channelCount: NotRequired[ULongRange]
    deviceId: NotRequired[str]
    groupId: NotRequired[str]
    displaySurface: NotRequired[str]
    logicalSurface: NotRequired[bool]
    cursor: NotRequired[Sequence[str]]

class MediaTrackConstraintSet(TypedDict, TypedDict, TypedDict):
    whiteBalanceMode: NotRequired[ConstrainDOMString]
    exposureMode: NotRequired[ConstrainDOMString]
    focusMode: NotRequired[ConstrainDOMString]
    pointsOfInterest: NotRequired[ConstrainPoint2D]
    exposureCompensation: NotRequired[ConstrainDouble]
    exposureTime: NotRequired[ConstrainDouble]
    colorTemperature: NotRequired[ConstrainDouble]
    iso: NotRequired[ConstrainDouble]
    brightness: NotRequired[ConstrainDouble]
    contrast: NotRequired[ConstrainDouble]
    saturation: NotRequired[ConstrainDouble]
    sharpness: NotRequired[ConstrainDouble]
    focusDistance: NotRequired[ConstrainDouble]
    pan: NotRequired[bool | ConstrainDouble]
    tilt: NotRequired[bool | ConstrainDouble]
    zoom: NotRequired[bool | ConstrainDouble]
    torch: NotRequired[ConstrainBoolean]
    width: NotRequired[ConstrainULong]
    height: NotRequired[ConstrainULong]
    aspectRatio: NotRequired[ConstrainDouble]
    frameRate: NotRequired[ConstrainDouble]
    facingMode: NotRequired[ConstrainDOMString]
    resizeMode: NotRequired[ConstrainDOMString]
    sampleRate: NotRequired[ConstrainULong]
    sampleSize: NotRequired[ConstrainULong]
    echoCancellation: NotRequired[ConstrainBoolean]
    autoGainControl: NotRequired[ConstrainBoolean]
    noiseSuppression: NotRequired[ConstrainBoolean]
    latency: NotRequired[ConstrainDouble]
    channelCount: NotRequired[ConstrainULong]
    deviceId: NotRequired[ConstrainDOMString]
    groupId: NotRequired[ConstrainDOMString]
    displaySurface: NotRequired[ConstrainDOMString]
    logicalSurface: NotRequired[ConstrainBoolean]
    cursor: NotRequired[ConstrainDOMString]
    restrictOwnAudio: NotRequired[ConstrainBoolean]
    suppressLocalAudioPlayback: NotRequired[ConstrainBoolean]

class MediaTrackSettings(TypedDict, TypedDict, TypedDict):
    whiteBalanceMode: NotRequired[str]
    exposureMode: NotRequired[str]
    focusMode: NotRequired[str]
    pointsOfInterest: NotRequired[Sequence[Point2D]]
    exposureCompensation: NotRequired[float]
    exposureTime: NotRequired[float]
    colorTemperature: NotRequired[float]
    iso: NotRequired[float]
    brightness: NotRequired[float]
    contrast: NotRequired[float]
    saturation: NotRequired[float]
    sharpness: NotRequired[float]
    focusDistance: NotRequired[float]
    pan: NotRequired[float]
    tilt: NotRequired[float]
    zoom: NotRequired[float]
    torch: NotRequired[bool]
    width: NotRequired[int]
    height: NotRequired[int]
    aspectRatio: NotRequired[float]
    frameRate: NotRequired[float]
    facingMode: NotRequired[str]
    resizeMode: NotRequired[str]
    sampleRate: NotRequired[int]
    sampleSize: NotRequired[int]
    echoCancellation: NotRequired[bool]
    autoGainControl: NotRequired[bool]
    noiseSuppression: NotRequired[bool]
    latency: NotRequired[float]
    channelCount: NotRequired[int]
    deviceId: NotRequired[str]
    groupId: NotRequired[str]
    displaySurface: NotRequired[str]
    logicalSurface: NotRequired[bool]
    cursor: NotRequired[str]
    restrictOwnAudio: NotRequired[bool]
    suppressLocalAudioPlayback: NotRequired[bool]

class ConstrainPoint2DParameters(TypedDict):
    exact: NotRequired[Sequence[Point2D]]
    ideal: NotRequired[Sequence[Point2D]]

class Point2D(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]

class ImageResource(TypedDict):
    src: USVString
    sizes: NotRequired[str]
    type: NotRequired[str]
    label: NotRequired[str]

class Ink:
    def requestPresenter(self, param: InkPresenterParam | None = {}) -> Awaitable[InkPresenter]: ...

class InkPresenterParam(TypedDict):
    presentationArea: NotRequired[Element | None]

class InkPresenter:
    presentationArea: Element | None
    expectedImprovement: int
    def updateInkTrailStartPoint(self, event: PointerEvent, style: InkTrailStyle): ...

class InkTrailStyle(TypedDict):
    color: str
    diameter: float

class InputDeviceCapabilities:
    @classmethod
    def new(self, deviceInitDict: InputDeviceCapabilitiesInit | None = {}) -> InputDeviceCapabilities: ...
    firesTouchEvents: bool
    pointerMovementScrolls: bool

class InputDeviceCapabilitiesInit(TypedDict):
    firesTouchEvents: NotRequired[bool]
    pointerMovementScrolls: NotRequired[bool]

class UIEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: UIEventInit | None = {}) -> UIEvent: ...
    sourceCapabilities: InputDeviceCapabilities | None
    view: Window | None
    detail: int
    def initUIEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: Window | None = None, detailArg: int | None = 0): ...
    which: int

class UIEventInit(TypedDict, TypedDict, EventInit, TypedDict):
    sourceCapabilities: NotRequired[InputDeviceCapabilities | None]
    view: NotRequired[Window | None]
    detail: NotRequired[int]
    which: NotRequired[int]

class InputEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: InputEventInit | None = {}) -> InputEvent: ...
    dataTransfer: DataTransfer | None
    def getTargetRanges(self) -> Sequence[StaticRange]: ...
    data: str | None
    isComposing: bool
    inputType: str

class InputEventInit(TypedDict, TypedDict, UIEventInit):
    dataTransfer: NotRequired[DataTransfer | None]
    targetRanges: NotRequired[Sequence[StaticRange]]
    data: NotRequired[str | None]
    isComposing: NotRequired[bool]
    inputType: NotRequired[str]

class IntersectionObserver:
    @classmethod
    def new(self, callback: IntersectionObserverCallback, options: IntersectionObserverInit | None = {}) -> IntersectionObserver: ...
    root: Element | Document | None
    rootMargin: str
    thresholds: Sequence[float]
    def observe(self, target: Element): ...
    def unobserve(self, target: Element): ...
    def disconnect(self): ...
    def takeRecords(self) -> Sequence[IntersectionObserverEntry]: ...

class IntersectionObserverEntry:
    @classmethod
    def new(self, intersectionObserverEntryInit: IntersectionObserverEntryInit) -> IntersectionObserverEntry: ...
    time: DOMHighResTimeStamp
    rootBounds: DOMRectReadOnly | None
    boundingClientRect: DOMRectReadOnly
    intersectionRect: DOMRectReadOnly
    isIntersecting: bool
    intersectionRatio: float
    target: Element

class IntersectionObserverEntryInit(TypedDict):
    time: DOMHighResTimeStamp
    rootBounds: DOMRectInit | None
    boundingClientRect: DOMRectInit
    intersectionRect: DOMRectInit
    isIntersecting: bool
    intersectionRatio: float
    target: Element

class IntersectionObserverInit(TypedDict):
    root: NotRequired[Element | Document | None]
    rootMargin: NotRequired[str]
    threshold: NotRequired[float | Sequence[float]]

class InterventionReportBody(ReportBody):
    def toJSON(self) -> object: ...
    id: str
    message: str
    sourceFile: str | None
    lineNumber: int | None
    columnNumber: int | None

class IsInputPendingOptions(TypedDict):
    includeContinuous: NotRequired[bool]

class Scheduling:
    def isInputPending(self, isInputPendingOptions: IsInputPendingOptions | None = {}) -> bool: ...

class Profiler(EventTarget):
    @classmethod
    def new(self, options: ProfilerInitOptions) -> Profiler: ...
    sampleInterval: DOMHighResTimeStamp
    stopped: bool
    def stop(self) -> Awaitable[ProfilerTrace]: ...

class ProfilerTrace(TypedDict):
    resources: Sequence[ProfilerResource]
    frames: Sequence[ProfilerFrame]
    stacks: Sequence[ProfilerStack]
    samples: Sequence[ProfilerSample]

class ProfilerSample(TypedDict):
    timestamp: DOMHighResTimeStamp
    stackId: NotRequired[int]

class ProfilerStack(TypedDict):
    parentId: NotRequired[int]
    frameId: int

class ProfilerFrame(TypedDict):
    name: str
    resourceId: NotRequired[int]
    line: NotRequired[int]
    column: NotRequired[int]

class ProfilerInitOptions(TypedDict):
    sampleInterval: DOMHighResTimeStamp
    maxBufferSize: int

class JsonLd: ...

class JsonLdProcessor:
    @classmethod
    def new(self) -> JsonLdProcessor: ...

class RdfDataset:
    @classmethod
    def new(self) -> RdfDataset: ...
    defaultGraph: RdfGraph
    def add(self, graphName: USVString, graph: RdfGraph): ...

class RdfGraph:
    @classmethod
    def new(self) -> RdfGraph: ...
    def add(self, triple: RdfTriple): ...

class RdfTriple:
    @classmethod
    def new(self) -> RdfTriple: ...
    subject: USVString
    predicate: USVString
    object: USVString | RdfLiteral

class RdfLiteral:
    @classmethod
    def new(self) -> RdfLiteral: ...
    value: USVString
    datatype: USVString
    language: USVString | None

class JsonLdOptions(TypedDict, TypedDict):
    base: NotRequired[USVString | None]
    compactArrays: NotRequired[bool]
    compactToRelative: NotRequired[bool]
    documentLoader: NotRequired[LoadDocumentCallback | None]
    expandContext: NotRequired[JsonLdRecord | None | USVString]
    extractAllScripts: NotRequired[bool]
    frameExpansion: NotRequired[bool]
    ordered: NotRequired[bool]
    processingMode: NotRequired[USVString]
    produceGeneralizedRdf: NotRequired[bool]
    rdfDirection: NotRequired[USVString | None]
    useNativeTypes: NotRequired[bool]
    useRdfType: NotRequired[bool]
    embed: NotRequired[JsonLdEmbed | bool]
    explicit: NotRequired[bool]
    omitDefault: NotRequired[bool]
    omitGraph: NotRequired[bool]
    requireAll: NotRequired[bool]
    frameDefault: NotRequired[bool]

class LoadDocumentOptions(TypedDict):
    extractAllScripts: NotRequired[bool]
    profile: NotRequired[USVString]
    requestProfile: NotRequired[USVString | Sequence[USVString]]

class RemoteDocument:
    @classmethod
    def new(self) -> RemoteDocument: ...
    contentType: USVString
    contextUrl: USVString
    document: Any
    documentUrl: USVString
    profile: USVString

class JsonLdError(TypedDict):
    code: NotRequired[JsonLdErrorCode]
    message: NotRequired[USVString | None]

class JsonLdFramingError(TypedDict):
    code: NotRequired[JsonLdFramingErrorCode]
    message: NotRequired[USVString | None]

class Keyboard(EventTarget):
    def lock(self, keyCodes: Sequence[str] | None = []) -> Awaitable[None]: ...
    def unlock(self): ...
    def getLayoutMap(self) -> Awaitable[KeyboardLayoutMap]: ...
    onlayoutchange: EventHandler

class KeyboardLayoutMap: ...

class LargestContentfulPaint(PerformanceEntry):
    renderTime: DOMHighResTimeStamp
    loadTime: DOMHighResTimeStamp
    size: int
    id: str
    url: str
    element: Element | None
    def toJSON(self) -> object: ...

class LayoutShift(PerformanceEntry):
    value: float
    hadRecentInput: bool
    lastInputTime: DOMHighResTimeStamp
    sources: Sequence[LayoutShiftAttribution]
    def toJSON(self) -> object: ...

class LayoutShiftAttribution:
    node: Node | None
    previousRect: DOMRectReadOnly
    currentRect: DOMRectReadOnly

class QueryOptions(TypedDict):
    postscriptNames: NotRequired[Sequence[str]]

class FontData:
    def blob(self) -> Awaitable[Blob]: ...
    postscriptName: USVString
    fullName: USVString
    family: USVString
    style: USVString

class PerformanceLongTaskTiming(PerformanceEntry):
    attribution: Sequence[TaskAttributionTiming]
    def toJSON(self) -> object: ...

class TaskAttributionTiming(PerformanceEntry):
    containerType: str
    containerSrc: str
    containerId: str
    containerName: str
    def toJSON(self) -> object: ...

class Magnetometer(Sensor):
    @classmethod
    def new(self, sensorOptions: MagnetometerSensorOptions | None = {}) -> Magnetometer: ...
    x: float | None
    y: float | None
    z: float | None

class MagnetometerSensorOptions(TypedDict, SensorOptions):
    referenceFrame: NotRequired[MagnetometerLocalCoordinateSystem]

class UncalibratedMagnetometer(Sensor):
    @classmethod
    def new(self, sensorOptions: MagnetometerSensorOptions | None = {}) -> UncalibratedMagnetometer: ...
    x: float | None
    y: float | None
    z: float | None
    xBias: float | None
    yBias: float | None
    zBias: float | None

class MagnetometerReadingValues(TypedDict):
    x: float | None
    y: float | None
    z: float | None

class UncalibratedMagnetometerReadingValues(TypedDict):
    x: float | None
    y: float | None
    z: float | None
    xBias: float | None
    yBias: float | None
    zBias: float | None

class BeforeInstallPromptEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: EventInit | None = {}) -> BeforeInstallPromptEvent: ...
    def prompt(self) -> Awaitable[PromptResponseObject]: ...

class PromptResponseObject(TypedDict):
    userChoice: NotRequired[AppBannerPromptOutcome]

class MediaConfiguration(TypedDict):
    video: NotRequired[VideoConfiguration]
    audio: NotRequired[AudioConfiguration]

class MediaDecodingConfiguration(TypedDict, MediaConfiguration):
    type: MediaDecodingType
    keySystemConfiguration: NotRequired[MediaCapabilitiesKeySystemConfiguration]

class MediaEncodingConfiguration(TypedDict, MediaConfiguration):
    type: MediaEncodingType

class VideoConfiguration(TypedDict):
    contentType: str
    width: int
    height: int
    bitrate: int
    framerate: float
    hasAlphaChannel: NotRequired[bool]
    hdrMetadataType: NotRequired[HdrMetadataType]
    colorGamut: NotRequired[ColorGamut]
    transferFunction: NotRequired[TransferFunction]
    scalabilityMode: NotRequired[str]
    spatialScalability: NotRequired[bool]

class AudioConfiguration(TypedDict):
    contentType: str
    channels: NotRequired[str]
    bitrate: NotRequired[int]
    samplerate: NotRequired[int]
    spatialRendering: NotRequired[bool]

class MediaCapabilitiesKeySystemConfiguration(TypedDict):
    keySystem: str
    initDataType: NotRequired[str]
    distinctiveIdentifier: NotRequired[MediaKeysRequirement]
    persistentState: NotRequired[MediaKeysRequirement]
    sessionTypes: NotRequired[Sequence[str]]
    audio: NotRequired[KeySystemTrackConfiguration]
    video: NotRequired[KeySystemTrackConfiguration]

class KeySystemTrackConfiguration(TypedDict):
    robustness: NotRequired[str]
    encryptionScheme: NotRequired[str | None]

class MediaCapabilitiesInfo(TypedDict):
    supported: bool
    smooth: bool
    powerEfficient: bool

class MediaCapabilitiesDecodingInfo(TypedDict, MediaCapabilitiesInfo):
    keySystemAccess: MediaKeySystemAccess
    configuration: NotRequired[MediaDecodingConfiguration]

class MediaCapabilitiesEncodingInfo(TypedDict, MediaCapabilitiesInfo):
    configuration: NotRequired[MediaEncodingConfiguration]

class MediaCapabilities:
    def decodingInfo(self, configuration: MediaDecodingConfiguration) -> Awaitable[MediaCapabilitiesDecodingInfo]: ...
    def encodingInfo(self, configuration: MediaEncodingConfiguration) -> Awaitable[MediaCapabilitiesEncodingInfo]: ...

class VideoPlaybackQuality:
    creationTime: DOMHighResTimeStamp
    droppedVideoFrames: int
    totalVideoFrames: int
    corruptedVideoFrames: int

class MediaSource(EventTarget):
    @classmethod
    def new(self) -> MediaSource: ...
    handle: MediaSourceHandle
    sourceBuffers: SourceBufferList
    activeSourceBuffers: SourceBufferList
    readyState: ReadyState
    duration: float
    onsourceopen: EventHandler
    onsourceended: EventHandler
    onsourceclose: EventHandler
    def addSourceBuffer(self, type: str) -> SourceBuffer: ...
    def removeSourceBuffer(self, sourceBuffer: SourceBuffer): ...
    def endOfStream(self, error: EndOfStreamError | None = None): ...
    def setLiveSeekableRange(self, start: float, end: float): ...
    def clearLiveSeekableRange(self): ...

class MediaSourceHandle: ...

class SourceBuffer(EventTarget):
    mode: AppendMode
    updating: bool
    buffered: TimeRanges
    timestampOffset: float
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList
    appendWindowStart: float
    appendWindowEnd: float
    onupdatestart: EventHandler
    onupdate: EventHandler
    onupdateend: EventHandler
    onerror: EventHandler
    onabort: EventHandler
    def appendBuffer(self, data: BufferSource): ...
    def abort(self): ...
    def changeType(self, type: str): ...
    def remove(self, start: float, end: float): ...

class SourceBufferList(EventTarget):
    length: int
    onaddsourcebuffer: EventHandler
    onremovesourcebuffer: EventHandler

class MockCapturePromptResultConfiguration(TypedDict):
    getUserMedia: NotRequired[MockCapturePromptResult]
    getDisplayMedia: NotRequired[MockCapturePromptResult]

class MockCaptureDeviceConfiguration(TypedDict):
    label: NotRequired[str]
    deviceId: NotRequired[str]
    groupId: NotRequired[str]

class MockCameraConfiguration(TypedDict, MockCaptureDeviceConfiguration):
    defaultFrameRate: NotRequired[float]
    facingMode: NotRequired[str]

class MockMicrophoneConfiguration(TypedDict, MockCaptureDeviceConfiguration):
    defaultSampleRate: NotRequired[int]

class CanvasCaptureMediaStreamTrack(MediaStreamTrack):
    canvas: HTMLCanvasElement
    def requestFrame(self): ...

class CaptureActionEvent(Event):
    @classmethod
    def new(self, init: CaptureActionEventInit | None = {}) -> CaptureActionEvent: ...
    action: CaptureAction

class CaptureActionEventInit(TypedDict, EventInit):
    action: NotRequired[str]

class CropTarget: ...

class BrowserCaptureMediaStreamTrack(MediaStreamTrack):
    def cropTo(self, cropTarget: CropTarget | None) -> Awaitable[None]: ...
    def clone(self) -> BrowserCaptureMediaStreamTrack: ...

class MediaStream(EventTarget):
    @overload
    @classmethod
    def new(self) -> MediaStream: ...
    @overload
    @classmethod
    def new(self, stream: MediaStream) -> MediaStream: ...
    @overload
    @classmethod
    def new(self, tracks: Sequence[MediaStreamTrack]) -> MediaStream: ...
    id: str
    def getAudioTracks(self) -> Sequence[MediaStreamTrack]: ...
    def getVideoTracks(self) -> Sequence[MediaStreamTrack]: ...
    def getTracks(self) -> Sequence[MediaStreamTrack]: ...
    def getTrackById(self, trackId: str) -> MediaStreamTrack | None: ...
    def addTrack(self, track: MediaStreamTrack): ...
    def removeTrack(self, track: MediaStreamTrack): ...
    def clone(self) -> MediaStream: ...
    active: bool
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class MediaTrackConstraints(TypedDict, MediaTrackConstraintSet):
    advanced: NotRequired[Sequence[MediaTrackConstraintSet]]

class MediaStreamTrackEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: MediaStreamTrackEventInit) -> MediaStreamTrackEvent: ...
    track: MediaStreamTrack

class MediaStreamTrackEventInit(TypedDict, EventInit):
    track: MediaStreamTrack

class OverconstrainedError(DOMException):
    @classmethod
    def new(self, constraint: str, message: str | None = "") -> OverconstrainedError: ...
    constraint: str

class MediaDeviceInfo:
    deviceId: str
    kind: MediaDeviceKind
    label: str
    groupId: str
    def toJSON(self) -> object: ...

class InputDeviceInfo(MediaDeviceInfo):
    def getCapabilities(self) -> MediaTrackCapabilities: ...

class MediaStreamConstraints(TypedDict, TypedDict, TypedDict):
    video: NotRequired[bool | MediaTrackConstraints]
    audio: NotRequired[bool | MediaTrackConstraints]
    preferCurrentTab: NotRequired[bool]
    peerIdentity: NotRequired[str]

class DoubleRange(TypedDict):
    max: NotRequired[float]
    min: NotRequired[float]

class ConstrainDoubleRange(TypedDict, DoubleRange):
    exact: NotRequired[float]
    ideal: NotRequired[float]

class ULongRange(TypedDict):
    max: NotRequired[int]
    min: NotRequired[int]

class ConstrainULongRange(TypedDict, ULongRange):
    exact: NotRequired[int]
    ideal: NotRequired[int]

class ConstrainBooleanParameters(TypedDict):
    exact: NotRequired[bool]
    ideal: NotRequired[bool]

class ConstrainDOMStringParameters(TypedDict):
    exact: NotRequired[str | Sequence[str]]
    ideal: NotRequired[str | Sequence[str]]

class DevicePermissionDescriptor(TypedDict, PermissionDescriptor):
    deviceId: NotRequired[str]

class CameraDevicePermissionDescriptor(TypedDict, DevicePermissionDescriptor):
    panTiltZoom: NotRequired[bool]

class MediaStreamTrackProcessor:
    @classmethod
    def new(self, init: MediaStreamTrackProcessorInit) -> MediaStreamTrackProcessor: ...
    readable: ReadableStream

class MediaStreamTrackProcessorInit(TypedDict):
    track: MediaStreamTrack
    maxBufferSize: NotRequired[int]

class VideoTrackGenerator:
    @classmethod
    def new(self) -> VideoTrackGenerator: ...
    writable: WritableStream
    muted: bool
    track: MediaStreamTrack

class ViewportMediaStreamConstraints(TypedDict):
    video: NotRequired[bool | MediaTrackConstraints]
    audio: NotRequired[bool | MediaTrackConstraints]

class MediaSession:
    metadata: MediaMetadata | None
    playbackState: MediaSessionPlaybackState
    def setActionHandler(self, action: MediaSessionAction, handler: MediaSessionActionHandler | None): ...
    def setPositionState(self, state: MediaPositionState | None = {}): ...
    def setMicrophoneActive(self, active: bool): ...
    def setCameraActive(self, active: bool): ...

class MediaMetadata:
    @classmethod
    def new(self, init: MediaMetadataInit | None = {}) -> MediaMetadata: ...
    title: str
    artist: str
    album: str
    artwork: Sequence[MediaImage]

class MediaMetadataInit(TypedDict):
    title: NotRequired[str]
    artist: NotRequired[str]
    album: NotRequired[str]
    artwork: NotRequired[Sequence[MediaImage]]

class MediaImage(TypedDict):
    src: USVString
    sizes: NotRequired[str]
    type: NotRequired[str]

class MediaPositionState(TypedDict):
    duration: NotRequired[float]
    playbackRate: NotRequired[float]
    position: NotRequired[float]

class MediaSessionActionDetails(TypedDict):
    action: MediaSessionAction
    seekOffset: NotRequired[float]
    seekTime: NotRequired[float]
    fastSeek: NotRequired[bool]

class MediaRecorder(EventTarget):
    @classmethod
    def new(self, stream: MediaStream, options: MediaRecorderOptions | None = {}) -> MediaRecorder: ...
    stream: MediaStream
    mimeType: str
    state: RecordingState
    onstart: EventHandler
    onstop: EventHandler
    ondataavailable: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onerror: EventHandler
    videoBitsPerSecond: int
    audioBitsPerSecond: int
    audioBitrateMode: BitrateMode
    def start(self, timeslice: int | None = None): ...
    def stop(self): ...
    def pause(self): ...
    def resume(self): ...
    def requestData(self): ...

class MediaRecorderOptions(TypedDict):
    mimeType: NotRequired[str]
    audioBitsPerSecond: NotRequired[int]
    videoBitsPerSecond: NotRequired[int]
    bitsPerSecond: NotRequired[int]
    audioBitrateMode: NotRequired[BitrateMode]

class BlobEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: BlobEventInit) -> BlobEvent: ...
    data: Blob
    timecode: DOMHighResTimeStamp

class BlobEventInit(TypedDict):
    data: Blob
    timecode: NotRequired[DOMHighResTimeStamp]

class HTMLModelElement(HTMLElement): ...

class RTCRtpSendParameters(TypedDict, TypedDict, RTCRtpParameters):
    degradationPreference: NotRequired[RTCDegradationPreference]
    transactionId: str
    encodings: Sequence[RTCRtpEncodingParameters]

class Navigation(EventTarget):
    def entries(self) -> Sequence[NavigationHistoryEntry]: ...
    currentEntry: NavigationHistoryEntry | None
    def updateCurrentEntry(self, options: NavigationUpdateCurrentEntryOptions): ...
    transition: NavigationTransition | None
    canGoBack: bool
    canGoForward: bool
    def navigate(self, url: USVString, options: NavigationNavigateOptions | None = {}) -> NavigationResult: ...
    def reload(self, options: NavigationReloadOptions | None = {}) -> NavigationResult: ...
    def traverseTo(self, key: str, options: NavigationOptions | None = {}) -> NavigationResult: ...
    def back(self, options: NavigationOptions | None = {}) -> NavigationResult: ...
    def forward(self, options: NavigationOptions | None = {}) -> NavigationResult: ...
    onnavigate: EventHandler
    onnavigatesuccess: EventHandler
    onnavigateerror: EventHandler
    oncurrententrychange: EventHandler

class NavigationUpdateCurrentEntryOptions(TypedDict):
    state: Any

class NavigationOptions(TypedDict):
    info: NotRequired[Any]

class NavigationNavigateOptions(TypedDict, NavigationOptions):
    state: NotRequired[Any]
    history: NotRequired[NavigationHistoryBehavior]

class NavigationReloadOptions(TypedDict, NavigationOptions):
    state: NotRequired[Any]

class NavigationResult(TypedDict):
    committed: NotRequired[Awaitable[NavigationHistoryEntry]]
    finished: NotRequired[Awaitable[NavigationHistoryEntry]]

class NavigationCurrentEntryChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInit: NavigationCurrentEntryChangeEventInit) -> NavigationCurrentEntryChangeEvent: ...
    navigationType: NavigationType | None
    from_: NavigationHistoryEntry

class NavigationCurrentEntryChangeEventInit(TypedDict, EventInit):
    navigationType: NotRequired[NavigationType | None]
    destination: NavigationHistoryEntry

class NavigationTransition:
    navigationType: NavigationType
    from_: NavigationHistoryEntry
    finished: Awaitable[None]

class NavigateEvent(Event):
    @classmethod
    def new(self, type: str, eventInit: NavigateEventInit) -> NavigateEvent: ...
    navigationType: NavigationType
    destination: NavigationDestination
    canIntercept: bool
    userInitiated: bool
    hashChange: bool
    signal: AbortSignal
    formData: FormData | None
    downloadRequest: str | None
    info: Any
    def intercept(self, options: NavigationInterceptOptions | None = {}): ...
    def scroll(self): ...

class NavigateEventInit(TypedDict, EventInit):
    navigationType: NotRequired[NavigationType]
    destination: NavigationDestination
    canIntercept: NotRequired[bool]
    userInitiated: NotRequired[bool]
    hashChange: NotRequired[bool]
    signal: AbortSignal
    formData: NotRequired[FormData | None]
    downloadRequest: NotRequired[str | None]
    info: NotRequired[Any]

class NavigationInterceptOptions(TypedDict):
    handler: NotRequired[NavigationInterceptHandler]
    focusReset: NotRequired[NavigationFocusReset]
    scroll: NotRequired[NavigationScrollBehavior]

class NavigationDestination:
    url: USVString
    key: str | None
    id: str | None
    index: int
    sameDocument: bool
    def getState(self) -> Any: ...

class NavigationHistoryEntry(EventTarget):
    url: USVString | None
    key: str
    id: str
    index: int
    sameDocument: bool
    def getState(self) -> Any: ...
    ondispose: EventHandler

class PerformanceNavigationTiming(PerformanceResourceTiming):
    unloadEventStart: DOMHighResTimeStamp
    unloadEventEnd: DOMHighResTimeStamp
    domInteractive: DOMHighResTimeStamp
    domContentLoadedEventStart: DOMHighResTimeStamp
    domContentLoadedEventEnd: DOMHighResTimeStamp
    domComplete: DOMHighResTimeStamp
    loadEventStart: DOMHighResTimeStamp
    loadEventEnd: DOMHighResTimeStamp
    type: NavigationTimingType
    redirectCount: int
    def toJSON(self) -> object: ...
    activationStart: DOMHighResTimeStamp

class PerformanceTiming:
    navigationStart: int
    unloadEventStart: int
    unloadEventEnd: int
    redirectStart: int
    redirectEnd: int
    fetchStart: int
    domainLookupStart: int
    domainLookupEnd: int
    connectStart: int
    connectEnd: int
    secureConnectionStart: int
    requestStart: int
    responseStart: int
    responseEnd: int
    domLoading: int
    domInteractive: int
    domContentLoadedEventStart: int
    domContentLoadedEventEnd: int
    domComplete: int
    loadEventStart: int
    loadEventEnd: int
    def toJSON(self) -> object: ...

class PerformanceNavigation:
    TYPE_NAVIGATE = 0
    TYPE_RELOAD = 1
    TYPE_BACK_FORWARD = 2
    TYPE_RESERVED = 255
    type: int
    redirectCount: int
    def toJSON(self) -> object: ...

class NavigatorNetworkInformation:
    connection: NetworkInformation

class NetworkInformation(EventTarget, NetworkInformationSaveData):
    type: ConnectionType
    effectiveType: EffectiveConnectionType
    downlinkMax: Megabit
    downlink: Megabit
    rtt: Millisecond
    onchange: EventHandler

class Notification(EventTarget):
    @classmethod
    def new(self, title: str, options: NotificationOptions | None = {}) -> Notification: ...
    onclick: EventHandler
    onshow: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    title: str
    dir: NotificationDirection
    lang: str
    body: str
    tag: str
    image: USVString
    icon: USVString
    badge: USVString
    vibrate: Sequence[int]
    timestamp: EpochTimeStamp
    renotify: bool
    silent: bool
    requireInteraction: bool
    data: Any
    actions: Sequence[NotificationAction]
    def close(self): ...

class NotificationOptions(TypedDict):
    dir: NotRequired[NotificationDirection]
    lang: NotRequired[str]
    body: NotRequired[str]
    tag: NotRequired[str]
    image: NotRequired[USVString]
    icon: NotRequired[USVString]
    badge: NotRequired[USVString]
    vibrate: NotRequired[VibratePattern]
    timestamp: NotRequired[EpochTimeStamp]
    renotify: NotRequired[bool]
    silent: NotRequired[bool]
    requireInteraction: NotRequired[bool]
    data: NotRequired[Any]
    actions: NotRequired[Sequence[NotificationAction]]

class NotificationAction(TypedDict):
    action: str
    title: str
    icon: NotRequired[USVString]

class GetNotificationOptions(TypedDict):
    tag: NotRequired[str]

class NotificationEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: NotificationEventInit) -> NotificationEvent: ...
    notification: Notification
    action: str

class NotificationEventInit(TypedDict, ExtendableEventInit):
    notification: Notification
    action: NotRequired[str]

class DeviceOrientationEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: DeviceOrientationEventInit | None = {}) -> DeviceOrientationEvent: ...
    alpha: float | None
    beta: float | None
    gamma: float | None
    absolute: bool

class DeviceOrientationEventInit(TypedDict, EventInit):
    alpha: NotRequired[float | None]
    beta: NotRequired[float | None]
    gamma: NotRequired[float | None]
    absolute: NotRequired[bool]

class DeviceMotionEventAcceleration:
    x: float | None
    y: float | None
    z: float | None

class DeviceMotionEventRotationRate:
    alpha: float | None
    beta: float | None
    gamma: float | None

class DeviceMotionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: DeviceMotionEventInit | None = {}) -> DeviceMotionEvent: ...
    acceleration: DeviceMotionEventAcceleration | None
    accelerationIncludingGravity: DeviceMotionEventAcceleration | None
    rotationRate: DeviceMotionEventRotationRate | None
    interval: float

class DeviceMotionEventAccelerationInit(TypedDict):
    x: NotRequired[float | None]
    y: NotRequired[float | None]
    z: NotRequired[float | None]

class DeviceMotionEventRotationRateInit(TypedDict):
    alpha: NotRequired[float | None]
    beta: NotRequired[float | None]
    gamma: NotRequired[float | None]

class DeviceMotionEventInit(TypedDict, EventInit):
    acceleration: NotRequired[DeviceMotionEventAccelerationInit]
    accelerationIncludingGravity: NotRequired[DeviceMotionEventAccelerationInit]
    rotationRate: NotRequired[DeviceMotionEventRotationRateInit]
    interval: NotRequired[float]

class OrientationSensor(Sensor):
    quaternion: Sequence[float]
    def populateMatrix(self, targetMatrix: RotationMatrixType): ...

class OrientationSensorOptions(TypedDict, SensorOptions):
    referenceFrame: NotRequired[OrientationSensorLocalCoordinateSystem]

class AbsoluteOrientationSensor(OrientationSensor):
    @classmethod
    def new(self, sensorOptions: OrientationSensorOptions | None = {}) -> AbsoluteOrientationSensor: ...

class RelativeOrientationSensor(OrientationSensor):
    @classmethod
    def new(self, sensorOptions: OrientationSensorOptions | None = {}) -> RelativeOrientationSensor: ...

class AbsoluteOrientationReadingValues(TypedDict):
    quaternion: Sequence[float]

class RelativeOrientationReadingValues(TypedDict, AbsoluteOrientationReadingValues): ...

class Client:
    lifecycleState: ClientLifecycleState
    url: USVString
    frameType: FrameType
    id: str
    type: ClientType
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]): ...
    @overload
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...

class PerformancePaintTiming(PerformanceEntry): ...

class PaymentManager:
    instruments: PaymentInstruments
    userHint: str
    def enableDelegations(self, delegations: Sequence[PaymentDelegation]) -> Awaitable[None]: ...

class PaymentInstruments:
    def delete(self, instrumentKey: str) -> Awaitable[bool]: ...
    def get(self, instrumentKey: str) -> Awaitable[Any]: ...
    def keys(self) -> Awaitable[Sequence[str]]: ...
    def has(self, instrumentKey: str) -> Awaitable[bool]: ...
    def set(self, instrumentKey: str, details: PaymentInstrument) -> Awaitable[None]: ...
    def clear(self) -> Awaitable[None]: ...

class PaymentInstrument(TypedDict):
    name: str
    icons: NotRequired[Sequence[ImageObject]]
    method: NotRequired[str]

class ImageObject(TypedDict):
    src: USVString
    sizes: NotRequired[str]
    type: NotRequired[str]

class CanMakePaymentEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str) -> CanMakePaymentEvent: ...
    def respondWith(self, canMakePaymentResponse: Awaitable[bool]): ...

class PaymentRequestDetailsUpdate(TypedDict):
    error: NotRequired[str]
    total: NotRequired[PaymentCurrencyAmount]
    modifiers: NotRequired[Sequence[PaymentDetailsModifier]]
    shippingOptions: NotRequired[Sequence[PaymentShippingOption]]
    paymentMethodErrors: NotRequired[object]
    shippingAddressErrors: NotRequired[AddressErrors]

class PaymentRequestEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: PaymentRequestEventInit | None = {}) -> PaymentRequestEvent: ...
    topOrigin: USVString
    paymentRequestOrigin: USVString
    paymentRequestId: str
    methodData: Sequence[PaymentMethodData]
    total: object
    modifiers: Sequence[PaymentDetailsModifier]
    paymentOptions: object | None
    shippingOptions: Sequence[PaymentShippingOption]
    def openWindow(self, url: USVString) -> Awaitable[WindowClient | None]: ...
    def changePaymentMethod(self, methodName: str, methodDetails: object | None = None) -> Awaitable[PaymentRequestDetailsUpdate | None]: ...
    def changeShippingAddress(self, shippingAddress: AddressInit | None = {}) -> Awaitable[PaymentRequestDetailsUpdate | None]: ...
    def changeShippingOption(self, shippingOption: str) -> Awaitable[PaymentRequestDetailsUpdate | None]: ...
    def respondWith(self, handlerResponsePromise: Awaitable[PaymentHandlerResponse]): ...

class PaymentRequestEventInit(TypedDict, ExtendableEventInit):
    topOrigin: NotRequired[USVString]
    paymentRequestOrigin: NotRequired[USVString]
    paymentRequestId: NotRequired[str]
    methodData: NotRequired[Sequence[PaymentMethodData]]
    total: NotRequired[PaymentCurrencyAmount]
    modifiers: NotRequired[Sequence[PaymentDetailsModifier]]
    paymentOptions: NotRequired[PaymentOptions]
    shippingOptions: NotRequired[Sequence[PaymentShippingOption]]

class PaymentHandlerResponse(TypedDict):
    methodName: NotRequired[str]
    details: NotRequired[object]
    payerName: NotRequired[str | None]
    payerEmail: NotRequired[str | None]
    payerPhone: NotRequired[str | None]
    shippingAddress: NotRequired[AddressInit]
    shippingOption: NotRequired[str | None]

class AddressInit(TypedDict):
    country: NotRequired[str]
    addressLine: NotRequired[Sequence[str]]
    region: NotRequired[str]
    city: NotRequired[str]
    dependentLocality: NotRequired[str]
    postalCode: NotRequired[str]
    sortingCode: NotRequired[str]
    organization: NotRequired[str]
    recipient: NotRequired[str]
    phone: NotRequired[str]

class PaymentOptions(TypedDict):
    requestPayerName: NotRequired[bool]
    requestBillingAddress: NotRequired[bool]
    requestPayerEmail: NotRequired[bool]
    requestPayerPhone: NotRequired[bool]
    requestShipping: NotRequired[bool]
    shippingType: NotRequired[PaymentShippingType]

class PaymentShippingOption(TypedDict):
    id: str
    label: str
    amount: PaymentCurrencyAmount
    selected: NotRequired[bool]

class AddressErrors(TypedDict):
    addressLine: NotRequired[str]
    city: NotRequired[str]
    country: NotRequired[str]
    dependentLocality: NotRequired[str]
    organization: NotRequired[str]
    phone: NotRequired[str]
    postalCode: NotRequired[str]
    recipient: NotRequired[str]
    region: NotRequired[str]
    sortingCode: NotRequired[str]

class PaymentRequest(EventTarget):
    @classmethod
    def new(self, methodData: Sequence[PaymentMethodData], details: PaymentDetailsInit) -> PaymentRequest: ...
    def show(self, detailsPromise: Awaitable[PaymentDetailsUpdate] | None = None) -> Awaitable[PaymentResponse]: ...
    def abort(self) -> Awaitable[None]: ...
    def canMakePayment(self) -> Awaitable[bool]: ...
    id: str
    onpaymentmethodchange: EventHandler

class PaymentMethodData(TypedDict):
    supportedMethods: str
    data: NotRequired[object]

class PaymentCurrencyAmount(TypedDict):
    currency: str
    value: str

class PaymentDetailsBase(TypedDict):
    displayItems: NotRequired[Sequence[PaymentItem]]
    modifiers: NotRequired[Sequence[PaymentDetailsModifier]]

class PaymentDetailsInit(TypedDict, PaymentDetailsBase):
    id: NotRequired[str]
    total: PaymentItem

class PaymentDetailsUpdate(TypedDict, PaymentDetailsBase):
    total: NotRequired[PaymentItem]
    paymentMethodErrors: NotRequired[object]

class PaymentDetailsModifier(TypedDict):
    supportedMethods: str
    total: NotRequired[PaymentItem]
    additionalDisplayItems: NotRequired[Sequence[PaymentItem]]
    data: NotRequired[object]

class PaymentItem(TypedDict):
    label: str
    amount: PaymentCurrencyAmount
    pending: NotRequired[bool]

class PaymentCompleteDetails(TypedDict):
    data: NotRequired[object | None]

class PaymentResponse(EventTarget):
    def toJSON(self) -> object: ...
    requestId: str
    methodName: str
    details: object
    def complete(self, result: PaymentComplete | None = "unknown", details: PaymentCompleteDetails | None = {}) -> Awaitable[None]: ...
    def retry(self, errorFields: PaymentValidationErrors | None = {}) -> Awaitable[None]: ...

class PaymentValidationErrors(TypedDict):
    error: NotRequired[str]
    paymentMethod: NotRequired[object]

class PaymentMethodChangeEvent(PaymentRequestUpdateEvent):
    @classmethod
    def new(self, type: str, eventInitDict: PaymentMethodChangeEventInit | None = {}) -> PaymentMethodChangeEvent: ...
    methodName: str
    methodDetails: object | None

class PaymentMethodChangeEventInit(TypedDict, PaymentRequestUpdateEventInit):
    methodName: NotRequired[str]
    methodDetails: NotRequired[object | None]

class PaymentRequestUpdateEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PaymentRequestUpdateEventInit | None = {}) -> PaymentRequestUpdateEvent: ...
    def updateWith(self, detailsPromise: Awaitable[PaymentDetailsUpdate]): ...

class PaymentRequestUpdateEventInit(TypedDict, EventInit): ...

class MemoryMeasurement(TypedDict):
    bytes: NotRequired[int]
    breakdown: NotRequired[Sequence[MemoryBreakdownEntry]]

class MemoryBreakdownEntry(TypedDict):
    bytes: NotRequired[int]
    attribution: NotRequired[Sequence[MemoryAttribution]]
    types: NotRequired[Sequence[str]]

class MemoryAttribution(TypedDict):
    url: NotRequired[USVString]
    container: NotRequired[MemoryAttributionContainer]
    scope: NotRequired[str]

class MemoryAttributionContainer(TypedDict):
    id: NotRequired[str]
    src: NotRequired[USVString]

class PerformanceEntry:
    name: str
    entryType: str
    startTime: DOMHighResTimeStamp
    duration: DOMHighResTimeStamp
    def toJSON(self) -> object: ...

class PerformanceObserver:
    @classmethod
    def new(self, callback: PerformanceObserverCallback) -> PerformanceObserver: ...
    def observe(self, options: PerformanceObserverInit | None = {}): ...
    def disconnect(self): ...
    def takeRecords(self) -> PerformanceEntryList: ...

class PerformanceObserverCallbackOptions(TypedDict):
    droppedEntriesCount: NotRequired[int]

class PerformanceObserverEntryList:
    def getEntries(self) -> PerformanceEntryList: ...
    def getEntriesByType(self, type: str) -> PerformanceEntryList: ...
    def getEntriesByName(self, name: str, type: str | None = None) -> PerformanceEntryList: ...

class PeriodicSyncManager:
    def register(self, tag: str, options: BackgroundSyncOptions | None = {}) -> Awaitable[None]: ...
    def getTags(self) -> Awaitable[Sequence[str]]: ...
    def unregister(self, tag: str) -> Awaitable[None]: ...

class BackgroundSyncOptions(TypedDict):
    minInterval: NotRequired[int]

class PeriodicSyncEventInit(TypedDict, ExtendableEventInit):
    tag: str

class PeriodicSyncEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, init: PeriodicSyncEventInit) -> PeriodicSyncEvent: ...
    tag: str

class PermissionsPolicy:
    def allowsFeature(self, feature: str, origin: str | None = None) -> bool: ...
    def features(self) -> Sequence[str]: ...
    def allowedFeatures(self) -> Sequence[str]: ...
    def getAllowlistForFeature(self, feature: str) -> Sequence[str]: ...

class PermissionsPolicyViolationReportBody(ReportBody):
    featureId: str
    sourceFile: str | None
    lineNumber: int | None
    columnNumber: int | None
    disposition: str

class Permissions:
    def request(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...
    def revoke(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...
    def query(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...

class PermissionDescriptor(TypedDict):
    name: str

class PermissionStatus(EventTarget):
    state: PermissionState
    name: str
    onchange: EventHandler

class PermissionSetParameters(TypedDict):
    descriptor: PermissionDescriptor
    state: PermissionState

class PictureInPictureWindow(EventTarget):
    width: int
    height: int
    onresize: EventHandler

class PictureInPictureEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PictureInPictureEventInit) -> PictureInPictureEvent: ...
    pictureInPictureWindow: PictureInPictureWindow

class PictureInPictureEventInit(TypedDict, EventInit):
    pictureInPictureWindow: PictureInPictureWindow

class PointerEventInit(TypedDict, MouseEventInit):
    pointerId: NotRequired[int]
    width: NotRequired[float]
    height: NotRequired[float]
    pressure: NotRequired[float]
    tangentialPressure: NotRequired[float]
    tiltX: NotRequired[int]
    tiltY: NotRequired[int]
    twist: NotRequired[int]
    altitudeAngle: NotRequired[float]
    azimuthAngle: NotRequired[float]
    pointerType: NotRequired[str]
    isPrimary: NotRequired[bool]
    coalescedEvents: NotRequired[Sequence[PointerEvent]]
    predictedEvents: NotRequired[Sequence[PointerEvent]]

class PointerEvent(MouseEvent):
    @classmethod
    def new(self, type: str, eventInitDict: PointerEventInit | None = {}) -> PointerEvent: ...
    pointerId: int
    width: float
    height: float
    pressure: float
    tangentialPressure: float
    tiltX: int
    tiltY: int
    twist: int
    altitudeAngle: float
    azimuthAngle: float
    pointerType: str
    isPrimary: bool
    def getCoalescedEvents(self) -> Sequence[PointerEvent]: ...
    def getPredictedEvents(self) -> Sequence[PointerEvent]: ...

class MouseEventInit(TypedDict, TypedDict, EventModifierInit):
    movementX: NotRequired[float]
    movementY: NotRequired[float]
    screenX: NotRequired[int]
    screenY: NotRequired[int]
    clientX: NotRequired[int]
    clientY: NotRequired[int]
    button: NotRequired[short]
    buttons: NotRequired[int]
    relatedTarget: NotRequired[EventTarget | None]

class HTMLPortalElement(HTMLElement):
    @classmethod
    def new(self) -> HTMLPortalElement: ...
    src: USVString
    referrerPolicy: str
    def activate(self, options: PortalActivateOptions | None = {}) -> Awaitable[None]: ...
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class PortalActivateOptions(TypedDict, StructuredSerializeOptions):
    data: NotRequired[Any]

class PortalHost(EventTarget):
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class PortalActivateEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PortalActivateEventInit | None = {}) -> PortalActivateEvent: ...
    data: Any
    def adoptPredecessor(self) -> HTMLPortalElement: ...

class PortalActivateEventInit(TypedDict, EventInit):
    data: NotRequired[Any]

class Presentation:
    defaultRequest: PresentationRequest | None
    receiver: PresentationReceiver | None

class PresentationRequest(EventTarget):
    @overload
    @classmethod
    def new(self, url: USVString) -> PresentationRequest: ...
    @overload
    @classmethod
    def new(self, urls: Sequence[USVString]) -> PresentationRequest: ...
    def start(self) -> Awaitable[PresentationConnection]: ...
    def reconnect(self, presentationId: USVString) -> Awaitable[PresentationConnection]: ...
    def getAvailability(self) -> Awaitable[PresentationAvailability]: ...
    onconnectionavailable: EventHandler

class PresentationAvailability(EventTarget):
    value: bool
    onchange: EventHandler

class PresentationConnectionAvailableEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PresentationConnectionAvailableEventInit) -> PresentationConnectionAvailableEvent: ...
    connection: PresentationConnection

class PresentationConnectionAvailableEventInit(TypedDict, EventInit):
    connection: PresentationConnection

class PresentationConnection(EventTarget):
    id: USVString
    url: USVString
    state: PresentationConnectionState
    def close(self): ...
    def terminate(self): ...
    onconnect: EventHandler
    onclose: EventHandler
    onterminate: EventHandler
    binaryType: BinaryType
    onmessage: EventHandler
    @overload
    def send(self, message: str): ...
    @overload
    def send(self, data: Blob): ...
    @overload
    def send(self, data: ArrayBuffer): ...
    @overload
    def send(self, data: ArrayBufferView): ...

class PresentationConnectionCloseEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: PresentationConnectionCloseEventInit) -> PresentationConnectionCloseEvent: ...
    reason: PresentationConnectionCloseReason
    message: str

class PresentationConnectionCloseEventInit(TypedDict, EventInit):
    reason: PresentationConnectionCloseReason
    message: NotRequired[str]

class PresentationReceiver:
    connectionList: Awaitable[PresentationConnectionList]

class PresentationConnectionList(EventTarget):
    connections: Sequence[PresentationConnection]
    onconnectionavailable: EventHandler

class ProximitySensor(Sensor):
    @classmethod
    def new(self, sensorOptions: SensorOptions | None = {}) -> ProximitySensor: ...
    distance: float | None
    max: float | None
    near: bool | None

class ProximityReadingValues(TypedDict):
    distance: float | None
    max: float | None
    near: bool | None

class PushPermissionDescriptor(TypedDict, PermissionDescriptor):
    userVisibleOnly: NotRequired[bool]

class PushManager:
    def subscribe(self, options: PushSubscriptionOptionsInit | None = {}) -> Awaitable[PushSubscription]: ...
    def getSubscription(self) -> Awaitable[PushSubscription | None]: ...
    def permissionState(self, options: PushSubscriptionOptionsInit | None = {}) -> Awaitable[PermissionState]: ...

class PushSubscriptionOptions:
    userVisibleOnly: bool
    applicationServerKey: ArrayBuffer

class PushSubscriptionOptionsInit(TypedDict):
    userVisibleOnly: NotRequired[bool]
    applicationServerKey: NotRequired[BufferSource | str | None]

class PushSubscription:
    endpoint: USVString
    expirationTime: EpochTimeStamp | None
    options: PushSubscriptionOptions
    def getKey(self, name: PushEncryptionKeyName) -> ArrayBuffer: ...
    def unsubscribe(self) -> Awaitable[bool]: ...
    def toJSON(self) -> PushSubscriptionJSON: ...

class PushSubscriptionJSON(TypedDict):
    endpoint: NotRequired[USVString]
    expirationTime: NotRequired[EpochTimeStamp | None]
    keys: NotRequired[USVString]

class PushMessageData:
    def arrayBuffer(self) -> ArrayBuffer: ...
    def blob(self) -> Blob: ...
    def json(self) -> Any: ...
    def text(self) -> USVString: ...

class PushEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: PushEventInit | None = {}) -> PushEvent: ...
    data: PushMessageData | None

class PushEventInit(TypedDict, ExtendableEventInit):
    data: NotRequired[PushMessageDataInit]

class PushSubscriptionChangeEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: PushSubscriptionChangeEventInit | None = {}) -> PushSubscriptionChangeEvent: ...
    newSubscription: PushSubscription | None
    oldSubscription: PushSubscription | None

class PushSubscriptionChangeEventInit(TypedDict, ExtendableEventInit):
    newSubscription: NotRequired[PushSubscription]
    oldSubscription: NotRequired[PushSubscription]

class XRView:
    camera: XRCamera | None
    isFirstPersonObserver: bool
    eye: XREye
    projectionMatrix: Float32Array
    transform: XRRigidTransform
    recommendedViewportScale: float | None
    def requestViewportScale(self, scale: float | None): ...

class XRCamera:
    width: int
    height: int

class XRWebGLBinding:
    @classmethod
    def new(self, session: XRSession, context: XRWebGLRenderingContext) -> XRWebGLBinding: ...
    def getCameraImage(self, camera: XRCamera) -> WebGLTexture | None: ...
    def getDepthInformation(self, view: XRView) -> XRWebGLDepthInformation | None: ...
    def getReflectionCubeMap(self, lightProbe: XRLightProbe) -> WebGLTexture | None: ...
    nativeProjectionScaleFactor: float
    usesDepthValues: bool
    def createProjectionLayer(self, init: XRProjectionLayerInit | None = {}) -> XRProjectionLayer: ...
    def createQuadLayer(self, init: XRQuadLayerInit | None = {}) -> XRQuadLayer: ...
    def createCylinderLayer(self, init: XRCylinderLayerInit | None = {}) -> XRCylinderLayer: ...
    def createEquirectLayer(self, init: XREquirectLayerInit | None = {}) -> XREquirectLayer: ...
    def createCubeLayer(self, init: XRCubeLayerInit | None = {}) -> XRCubeLayer: ...
    def getSubImage(self, layer: XRCompositionLayer, frame: XRFrame, eye: XREye | None = "none") -> XRWebGLSubImage: ...
    def getViewSubImage(self, layer: XRProjectionLayer, view: XRView) -> XRWebGLSubImage: ...

class RemotePlayback(EventTarget):
    def watchAvailability(self, callback: RemotePlaybackAvailabilityCallback) -> Awaitable[int]: ...
    def cancelWatchAvailability(self, id: int | None = None) -> Awaitable[None]: ...
    state: RemotePlaybackState
    onconnecting: EventHandler
    onconnect: EventHandler
    ondisconnect: EventHandler
    def prompt(self) -> Awaitable[None]: ...

class ReportBody:
    def toJSON(self) -> object: ...

class Report:
    def toJSON(self) -> object: ...
    type: str
    url: str
    body: ReportBody | None

class ReportingObserver:
    @classmethod
    def new(self, callback: ReportingObserverCallback, options: ReportingObserverOptions | None = {}) -> ReportingObserver: ...
    def observe(self): ...
    def disconnect(self): ...
    def takeRecords(self) -> ReportList: ...

class ReportingObserverOptions(TypedDict):
    types: NotRequired[Sequence[str]]
    buffered: NotRequired[bool]

class GenerateTestReportParameters(TypedDict):
    message: str
    group: NotRequired[str]

class IdleRequestOptions(TypedDict):
    timeout: NotRequired[int]

class IdleDeadline:
    def timeRemaining(self) -> DOMHighResTimeStamp: ...
    didTimeout: bool

class ResizeObserverOptions(TypedDict):
    box: NotRequired[ResizeObserverBoxOptions]

class ResizeObserver:
    @classmethod
    def new(self, callback: ResizeObserverCallback) -> ResizeObserver: ...
    def observe(self, target: Element, options: ResizeObserverOptions | None = {}): ...
    def unobserve(self, target: Element): ...
    def disconnect(self): ...

class ResizeObserverEntry:
    target: Element
    contentRect: DOMRectReadOnly
    borderBoxSize: Sequence[ResizeObserverSize]
    contentBoxSize: Sequence[ResizeObserverSize]
    devicePixelContentBoxSize: Sequence[ResizeObserverSize]

class ResizeObserverSize:
    inlineSize: float
    blockSize: float

class PerformanceResourceTiming(PerformanceEntry):
    initiatorType: str
    nextHopProtocol: ByteString
    workerStart: DOMHighResTimeStamp
    redirectStart: DOMHighResTimeStamp
    redirectEnd: DOMHighResTimeStamp
    fetchStart: DOMHighResTimeStamp
    domainLookupStart: DOMHighResTimeStamp
    domainLookupEnd: DOMHighResTimeStamp
    connectStart: DOMHighResTimeStamp
    connectEnd: DOMHighResTimeStamp
    secureConnectionStart: DOMHighResTimeStamp
    requestStart: DOMHighResTimeStamp
    responseStart: DOMHighResTimeStamp
    responseEnd: DOMHighResTimeStamp
    transferSize: int
    encodedBodySize: int
    decodedBodySize: int
    responseStatus: int
    renderBlockingStatus: RenderBlockingStatusType
    def toJSON(self) -> object: ...
    serverTiming: Sequence[PerformanceServerTiming]

class Sanitizer:
    @classmethod
    def new(self, config: SanitizerConfig | None = {}) -> Sanitizer: ...
    def sanitize(self, input: Document | DocumentFragment) -> DocumentFragment: ...
    def sanitizeFor(self, element: str, input: str) -> Element | None: ...
    def getConfiguration(self) -> SanitizerConfig: ...

class SetHTMLOptions(TypedDict):
    sanitizer: NotRequired[Sanitizer]

class SanitizerConfig(TypedDict):
    allowElements: NotRequired[Sequence[str]]
    blockElements: NotRequired[Sequence[str]]
    dropElements: NotRequired[Sequence[str]]
    allowAttributes: NotRequired[AttributeMatchList]
    dropAttributes: NotRequired[AttributeMatchList]
    allowCustomElements: NotRequired[bool]
    allowUnknownMarkup: NotRequired[bool]
    allowComments: NotRequired[bool]

class NetworkInformationSaveData:
    saveData: bool

class SchedulerPostTaskOptions(TypedDict):
    signal: NotRequired[AbortSignal]
    priority: NotRequired[TaskPriority]
    delay: NotRequired[int]

class Scheduler:
    def postTask(self, callback: SchedulerPostTaskCallback, options: SchedulerPostTaskOptions | None = {}) -> Awaitable[Any]: ...

class TaskPriorityChangeEvent(Event):
    @classmethod
    def new(self, type: str, priorityChangeEventInitDict: TaskPriorityChangeEventInit) -> TaskPriorityChangeEvent: ...
    previousPriority: TaskPriority

class TaskPriorityChangeEventInit(TypedDict, EventInit):
    previousPriority: TaskPriority

class TaskControllerInit(TypedDict):
    priority: NotRequired[TaskPriority]

class TaskController(AbortController):
    @classmethod
    def new(self, init: TaskControllerInit | None = {}) -> TaskController: ...
    def setPriority(self, priority: TaskPriority): ...

class TaskSignal(AbortSignal):
    priority: TaskPriority
    onprioritychange: EventHandler

class CaptureController:
    @classmethod
    def new(self) -> CaptureController: ...
    def setFocusBehavior(self, focusBehavior: CaptureStartFocusBehavior): ...

class DisplayMediaStreamOptions(TypedDict):
    video: NotRequired[bool | MediaTrackConstraints]
    audio: NotRequired[bool | MediaTrackConstraints]
    controller: NotRequired[CaptureController]
    selfBrowserSurface: NotRequired[SelfCapturePreferenceEnum]
    systemAudio: NotRequired[SystemAudioPreferenceEnum]
    surfaceSwitching: NotRequired[SurfaceSwitchingPreferenceEnum]

class ScreenOrientation(EventTarget):
    def lock(self, orientation: OrientationLockType) -> Awaitable[None]: ...
    def unlock(self): ...
    type: OrientationType
    angle: int
    onchange: EventHandler

class WakeLock:
    def request(self, type: WakeLockType | None = "screen") -> Awaitable[WakeLockSentinel]: ...

class WakeLockSentinel(EventTarget):
    released: bool
    type: WakeLockType
    def release(self) -> Awaitable[None]: ...
    onrelease: EventHandler

class ScrollTimelineOptions(TypedDict):
    source: NotRequired[Element | None]
    axis: NotRequired[ScrollAxis]

class ScrollTimeline(AnimationTimeline):
    @classmethod
    def new(self, options: ScrollTimelineOptions | None = {}) -> ScrollTimeline: ...
    source: Element | None
    axis: ScrollAxis

class ViewTimelineOptions(TypedDict):
    subject: NotRequired[Element]
    axis: NotRequired[ScrollAxis]

class ViewTimeline(ScrollTimeline):
    @classmethod
    def new(self, options: ViewTimelineOptions | None = {}) -> ViewTimeline: ...
    subject: Element
    startOffset: CSSNumericValue
    endOffset: CSSNumericValue

class AnimationTimeline:
    def getCurrentTime(self, rangeName: CSSOMString | None = None) -> CSSNumericValue | None: ...
    duration: CSSNumberish | None
    def play(self, effect: AnimationEffect | None = None) -> Animation: ...
    currentTime: float | None

class FragmentDirective: ...

class SecurePaymentConfirmationRequest(TypedDict):
    challenge: BufferSource
    rpId: USVString
    credentialIds: Sequence[BufferSource]
    instrument: PaymentCredentialInstrument
    timeout: NotRequired[int]
    payeeName: NotRequired[USVString]
    payeeOrigin: NotRequired[USVString]
    extensions: NotRequired[AuthenticationExtensionsClientInputs]
    locale: NotRequired[Sequence[USVString]]
    showOptOut: NotRequired[bool]

class AuthenticationExtensionsPaymentInputs(TypedDict):
    isPayment: NotRequired[bool]
    rpId: NotRequired[USVString]
    topOrigin: NotRequired[USVString]
    payeeName: NotRequired[USVString]
    payeeOrigin: NotRequired[USVString]
    total: NotRequired[PaymentCurrencyAmount]
    instrument: NotRequired[PaymentCredentialInstrument]

class CollectedClientPaymentData(TypedDict, CollectedClientData):
    payment: CollectedClientAdditionalPaymentData

class CollectedClientAdditionalPaymentData(TypedDict):
    rpId: USVString
    topOrigin: USVString
    payeeName: NotRequired[USVString]
    payeeOrigin: NotRequired[USVString]
    total: PaymentCurrencyAmount
    instrument: PaymentCredentialInstrument

class PaymentCredentialInstrument(TypedDict):
    displayName: USVString
    icon: USVString
    iconMustBeShown: NotRequired[bool]

class Selection:
    anchorNode: Node | None
    anchorOffset: int
    focusNode: Node | None
    focusOffset: int
    isCollapsed: bool
    rangeCount: int
    type: str
    def getRangeAt(self, index: int) -> Range: ...
    def addRange(self, range: Range): ...
    def removeRange(self, range: Range): ...
    def removeAllRanges(self): ...
    def empty(self): ...
    def getComposedRange(self, *shadowRoots: ShadowRoot) -> StaticRange: ...
    def collapse(self, node: Node | None, offset: int | None = 0): ...
    def setPosition(self, node: Node | None, offset: int | None = 0): ...
    def collapseToStart(self): ...
    def collapseToEnd(self): ...
    def extend(self, node: Node, offset: int | None = 0): ...
    def setBaseAndExtent(self, anchorNode: Node, anchorOffset: int, focusNode: Node, focusOffset: int): ...
    def selectAllChildren(self, node: Node): ...
    def modify(self, alter: str | None = None, direction: str | None = None, granularity: str | None = None): ...
    def deleteFromDocument(self): ...
    def containsNode(self, node: Node, allowPartialContainment: bool | None = false) -> bool: ...

class Serial(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    def getPorts(self) -> Awaitable[Sequence[SerialPort]]: ...
    def requestPort(self, options: SerialPortRequestOptions | None = {}) -> Awaitable[SerialPort]: ...

class SerialPortRequestOptions(TypedDict):
    filters: NotRequired[Sequence[SerialPortFilter]]

class SerialPortFilter(TypedDict):
    usbVendorId: NotRequired[int]
    usbProductId: NotRequired[int]

class SerialPort(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    readable: ReadableStream
    writable: WritableStream
    def getInfo(self) -> SerialPortInfo: ...
    def open(self, options: SerialOptions) -> Awaitable[None]: ...
    def setSignals(self, signals: SerialOutputSignals | None = {}) -> Awaitable[None]: ...
    def getSignals(self) -> Awaitable[SerialInputSignals]: ...
    def close(self) -> Awaitable[None]: ...
    def forget(self) -> Awaitable[None]: ...

class SerialPortInfo(TypedDict):
    usbVendorId: NotRequired[int]
    usbProductId: NotRequired[int]

class SerialOptions(TypedDict):
    baudRate: int
    dataBits: NotRequired[octet]
    stopBits: NotRequired[octet]
    parity: NotRequired[ParityType]
    bufferSize: NotRequired[int]
    flowControl: NotRequired[FlowControlType]

class SerialOutputSignals(TypedDict):
    dataTerminalReady: NotRequired[bool]
    requestToSend: NotRequired[bool]

class SerialInputSignals(TypedDict):
    dataCarrierDetect: bool
    clearToSend: bool
    ringIndicator: bool
    dataSetReady: bool

class PerformanceServerTiming:
    name: str
    duration: DOMHighResTimeStamp
    description: str
    def toJSON(self) -> object: ...

class ServiceWorker(EventTarget, AbstractWorker):
    scriptURL: USVString
    state: ServiceWorkerState
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]): ...
    @overload
    def postMessage(self, message: Any, options: StructuredSerializeOptions | None = {}): ...
    onstatechange: EventHandler

class ServiceWorkerContainer(EventTarget):
    controller: ServiceWorker | None
    ready: Awaitable[ServiceWorkerRegistration]
    def register(self, scriptURL: USVString, options: RegistrationOptions | None = {}) -> Awaitable[ServiceWorkerRegistration]: ...
    def getRegistration(self, clientURL: USVString | None = "") -> Awaitable[ServiceWorkerRegistration | None]: ...
    def getRegistrations(self) -> Awaitable[Sequence[ServiceWorkerRegistration]]: ...
    def startMessages(self): ...
    oncontrollerchange: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler

class RegistrationOptions(TypedDict):
    scope: NotRequired[USVString]
    type: NotRequired[WorkerType]
    updateViaCache: NotRequired[ServiceWorkerUpdateViaCache]

class NavigationPreloadManager:
    def enable(self) -> Awaitable[None]: ...
    def disable(self) -> Awaitable[None]: ...
    def setHeaderValue(self, value: ByteString) -> Awaitable[None]: ...
    def getState(self) -> Awaitable[NavigationPreloadState]: ...

class NavigationPreloadState(TypedDict):
    enabled: NotRequired[bool]
    headerValue: NotRequired[ByteString]

class WindowClient(Client):
    visibilityState: DocumentVisibilityState
    focused: bool
    ancestorOrigins: Sequence[USVString]
    def focus(self) -> Awaitable[WindowClient]: ...
    def navigate(self, url: USVString) -> Awaitable[WindowClient | None]: ...

class Clients:
    def get(self, id: str) -> Awaitable[Client | None]: ...
    def matchAll(self, options: ClientQueryOptions | None = {}) -> Awaitable[Sequence[Client]]: ...
    def openWindow(self, url: USVString) -> Awaitable[WindowClient | None]: ...
    def claim(self) -> Awaitable[None]: ...

class ClientQueryOptions(TypedDict):
    includeUncontrolled: NotRequired[bool]
    type: NotRequired[ClientType]

class ExtendableEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: ExtendableEventInit | None = {}) -> ExtendableEvent: ...
    def waitUntil(self, f: Awaitable[Any]): ...

class ExtendableEventInit(TypedDict, EventInit): ...

class FetchEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: FetchEventInit) -> FetchEvent: ...
    request: Request
    preloadResponse: Awaitable[Any]
    clientId: str
    resultingClientId: str
    replacesClientId: str
    handled: Awaitable[None]
    def respondWith(self, r: Awaitable[Response]): ...

class FetchEventInit(TypedDict, ExtendableEventInit):
    request: Request
    preloadResponse: NotRequired[Awaitable[Any]]
    clientId: NotRequired[str]
    resultingClientId: NotRequired[str]
    replacesClientId: NotRequired[str]
    handled: NotRequired[Awaitable[None]]

class ExtendableMessageEvent(ExtendableEvent):
    @classmethod
    def new(self, type: str, eventInitDict: ExtendableMessageEventInit | None = {}) -> ExtendableMessageEvent: ...
    data: Any
    origin: USVString
    lastEventId: str
    source: Client | ServiceWorker | MessagePort | None
    ports: Sequence[MessagePort]

class ExtendableMessageEventInit(TypedDict, ExtendableEventInit):
    data: NotRequired[Any]
    origin: NotRequired[USVString]
    lastEventId: NotRequired[str]
    source: NotRequired[Client | ServiceWorker | MessagePort | None]
    ports: NotRequired[Sequence[MessagePort]]

class Cache:
    def match(self, request: RequestInfo, options: CacheQueryOptions | None = {}) -> Awaitable[Response | None]: ...
    def matchAll(self, request: RequestInfo | None = None, options: CacheQueryOptions | None = {}) -> Awaitable[Sequence[Response]]: ...
    def add(self, request: RequestInfo) -> Awaitable[None]: ...
    def addAll(self, requests: Sequence[RequestInfo]) -> Awaitable[None]: ...
    def put(self, request: RequestInfo, response: Response) -> Awaitable[None]: ...
    def delete(self, request: RequestInfo, options: CacheQueryOptions | None = {}) -> Awaitable[bool]: ...
    def keys(self, request: RequestInfo | None = None, options: CacheQueryOptions | None = {}) -> Awaitable[Sequence[Request]]: ...

class CacheQueryOptions(TypedDict):
    ignoreSearch: NotRequired[bool]
    ignoreMethod: NotRequired[bool]
    ignoreVary: NotRequired[bool]

class CacheStorage:
    def match(self, request: RequestInfo, options: MultiCacheQueryOptions | None = {}) -> Awaitable[Response | None]: ...
    def has(self, cacheName: str) -> Awaitable[bool]: ...
    def open(self, cacheName: str) -> Awaitable[Cache]: ...
    def delete(self, cacheName: str) -> Awaitable[bool]: ...
    def keys(self) -> Awaitable[Sequence[str]]: ...

class MultiCacheQueryOptions(TypedDict, CacheQueryOptions):
    cacheName: NotRequired[str]

class FaceDetector:
    @classmethod
    def new(self, faceDetectorOptions: FaceDetectorOptions | None = {}) -> FaceDetector: ...
    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedFace]]: ...

class FaceDetectorOptions(TypedDict):
    maxDetectedFaces: NotRequired[int]
    fastMode: NotRequired[bool]

class DetectedFace(TypedDict):
    boundingBox: DOMRectReadOnly
    landmarks: Sequence[Landmark]

class Landmark(TypedDict):
    locations: Sequence[Point2D]
    type: NotRequired[LandmarkType]

class BarcodeDetector:
    @classmethod
    def new(self, barcodeDetectorOptions: BarcodeDetectorOptions | None = {}) -> BarcodeDetector: ...
    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedBarcode]]: ...

class BarcodeDetectorOptions(TypedDict):
    formats: NotRequired[Sequence[BarcodeFormat]]

class DetectedBarcode(TypedDict):
    boundingBox: DOMRectReadOnly
    rawValue: str
    format: BarcodeFormat
    cornerPoints: Sequence[Point2D]

class SpeechRecognition(EventTarget):
    @classmethod
    def new(self) -> SpeechRecognition: ...
    grammars: SpeechGrammarList
    lang: str
    continuous: bool
    interimResults: bool
    maxAlternatives: int
    def start(self): ...
    def stop(self): ...
    def abort(self): ...
    onaudiostart: EventHandler
    onsoundstart: EventHandler
    onspeechstart: EventHandler
    onspeechend: EventHandler
    onsoundend: EventHandler
    onaudioend: EventHandler
    onresult: EventHandler
    onnomatch: EventHandler
    onerror: EventHandler
    onstart: EventHandler
    onend: EventHandler

class SpeechRecognitionErrorEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: SpeechRecognitionErrorEventInit) -> SpeechRecognitionErrorEvent: ...
    error: SpeechRecognitionErrorCode
    message: str

class SpeechRecognitionErrorEventInit(TypedDict, EventInit):
    error: SpeechRecognitionErrorCode
    message: NotRequired[str]

class SpeechRecognitionAlternative:
    transcript: str
    confidence: float

class SpeechRecognitionResult:
    length: int
    isFinal: bool

class SpeechRecognitionResultList:
    length: int

class SpeechRecognitionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: SpeechRecognitionEventInit) -> SpeechRecognitionEvent: ...
    resultIndex: int
    results: SpeechRecognitionResultList

class SpeechRecognitionEventInit(TypedDict, EventInit):
    resultIndex: NotRequired[int]
    results: SpeechRecognitionResultList

class SpeechGrammar:
    src: str
    weight: float

class SpeechGrammarList:
    @classmethod
    def new(self) -> SpeechGrammarList: ...
    length: int
    def addFromURI(self, src: str, weight: float | None = 1.0): ...
    def addFromString(self, string: str, weight: float | None = 1.0): ...

class SpeechSynthesis(EventTarget):
    pending: bool
    speaking: bool
    paused: bool
    onvoiceschanged: EventHandler
    def speak(self, utterance: SpeechSynthesisUtterance): ...
    def cancel(self): ...
    def pause(self): ...
    def resume(self): ...
    def getVoices(self) -> Sequence[SpeechSynthesisVoice]: ...

class SpeechSynthesisUtterance(EventTarget):
    @classmethod
    def new(self, text: str | None = None) -> SpeechSynthesisUtterance: ...
    text: str
    lang: str
    voice: SpeechSynthesisVoice | None
    volume: float
    rate: float
    pitch: float
    onstart: EventHandler
    onend: EventHandler
    onerror: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onmark: EventHandler
    onboundary: EventHandler

class SpeechSynthesisEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: SpeechSynthesisEventInit) -> SpeechSynthesisEvent: ...
    utterance: SpeechSynthesisUtterance
    charIndex: int
    charLength: int
    elapsedTime: float
    name: str

class SpeechSynthesisEventInit(TypedDict, EventInit):
    utterance: SpeechSynthesisUtterance
    charIndex: NotRequired[int]
    charLength: NotRequired[int]
    elapsedTime: NotRequired[float]
    name: NotRequired[str]

class SpeechSynthesisErrorEvent(SpeechSynthesisEvent):
    @classmethod
    def new(self, type: str, eventInitDict: SpeechSynthesisErrorEventInit) -> SpeechSynthesisErrorEvent: ...
    error: SpeechSynthesisErrorCode

class SpeechSynthesisErrorEventInit(TypedDict, SpeechSynthesisEventInit):
    error: SpeechSynthesisErrorCode

class SpeechSynthesisVoice:
    voiceURI: str
    name: str
    lang: str
    localService: bool
    default: bool

class NavigatorStorage:
    storage: StorageManager

class StorageEstimate(TypedDict):
    usage: NotRequired[int]
    quota: NotRequired[int]

class ReadableStream:
    @classmethod
    def new(self, underlyingSource: object | None = None, strategy: QueuingStrategy | None = {}) -> ReadableStream: ...
    locked: bool
    def cancel(self, reason: Any | None = None) -> Awaitable[None]: ...
    def getReader(self, options: ReadableStreamGetReaderOptions | None = {}) -> ReadableStreamReader: ...
    def pipeThrough(self, transform: ReadableWritablePair, options: StreamPipeOptions | None = {}) -> ReadableStream: ...
    def pipeTo(self, destination: WritableStream, options: StreamPipeOptions | None = {}) -> Awaitable[None]: ...
    def tee(self) -> Sequence[ReadableStream]: ...

class ReadableStreamGetReaderOptions(TypedDict):
    mode: NotRequired[ReadableStreamReaderMode]

class ReadableStreamIteratorOptions(TypedDict):
    preventCancel: NotRequired[bool]

class ReadableWritablePair(TypedDict):
    readable: ReadableStream
    writable: WritableStream

class StreamPipeOptions(TypedDict):
    preventClose: NotRequired[bool]
    preventAbort: NotRequired[bool]
    preventCancel: NotRequired[bool]
    signal: NotRequired[AbortSignal]

class UnderlyingSource(TypedDict):
    start: NotRequired[UnderlyingSourceStartCallback]
    pull: NotRequired[UnderlyingSourcePullCallback]
    cancel: NotRequired[UnderlyingSourceCancelCallback]
    type: NotRequired[ReadableStreamType]
    autoAllocateChunkSize: NotRequired[int]

class ReadableStreamGenericReader:
    closed: Awaitable[None]
    def cancel(self, reason: Any | None = None) -> Awaitable[None]: ...

class ReadableStreamDefaultReader(ReadableStreamGenericReader):
    @classmethod
    def new(self, stream: ReadableStream) -> ReadableStreamDefaultReader: ...
    def read(self) -> Awaitable[ReadableStreamReadResult]: ...
    def releaseLock(self): ...

class ReadableStreamReadResult(TypedDict):
    value: NotRequired[Any]
    done: NotRequired[bool]

class ReadableStreamBYOBReader(ReadableStreamGenericReader):
    @classmethod
    def new(self, stream: ReadableStream) -> ReadableStreamBYOBReader: ...
    def read(self, view: ArrayBufferView) -> Awaitable[ReadableStreamReadResult]: ...
    def releaseLock(self): ...

class ReadableStreamDefaultController:
    desiredSize: float | None
    def close(self): ...
    def enqueue(self, chunk: Any | None = None): ...
    def error(self, e: Any | None = None): ...

class ReadableByteStreamController:
    byobRequest: ReadableStreamBYOBRequest | None
    desiredSize: float | None
    def close(self): ...
    def enqueue(self, chunk: ArrayBufferView): ...
    def error(self, e: Any | None = None): ...

class ReadableStreamBYOBRequest:
    view: ArrayBufferView | None
    def respond(self, bytesWritten: int): ...
    def respondWithNewView(self, view: ArrayBufferView): ...

class WritableStream:
    @classmethod
    def new(self, underlyingSink: object | None = None, strategy: QueuingStrategy | None = {}) -> WritableStream: ...
    locked: bool
    def abort(self, reason: Any | None = None) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def getWriter(self) -> WritableStreamDefaultWriter: ...

class UnderlyingSink(TypedDict):
    start: NotRequired[UnderlyingSinkStartCallback]
    write: NotRequired[UnderlyingSinkWriteCallback]
    close: NotRequired[UnderlyingSinkCloseCallback]
    abort: NotRequired[UnderlyingSinkAbortCallback]
    type: NotRequired[Any]

class WritableStreamDefaultWriter:
    @classmethod
    def new(self, stream: WritableStream) -> WritableStreamDefaultWriter: ...
    closed: Awaitable[None]
    desiredSize: float | None
    ready: Awaitable[None]
    def abort(self, reason: Any | None = None) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def releaseLock(self): ...
    def write(self, chunk: Any | None = None) -> Awaitable[None]: ...

class WritableStreamDefaultController:
    signal: AbortSignal
    def error(self, e: Any | None = None): ...

class TransformStream:
    @classmethod
    def new(self, transformer: object | None = None, writableStrategy: QueuingStrategy | None = {}, readableStrategy: QueuingStrategy | None = {}) -> TransformStream: ...
    readable: ReadableStream
    writable: WritableStream

class Transformer(TypedDict):
    start: NotRequired[TransformerStartCallback]
    transform: NotRequired[TransformerTransformCallback]
    flush: NotRequired[TransformerFlushCallback]
    readableType: NotRequired[Any]
    writableType: NotRequired[Any]

class TransformStreamDefaultController:
    desiredSize: float | None
    def enqueue(self, chunk: Any | None = None): ...
    def error(self, reason: Any | None = None): ...
    def terminate(self): ...

class QueuingStrategy(TypedDict):
    highWaterMark: NotRequired[float]
    size: NotRequired[QueuingStrategySize]

class QueuingStrategyInit(TypedDict):
    highWaterMark: float

class ByteLengthQueuingStrategy:
    @classmethod
    def new(self, init: QueuingStrategyInit) -> ByteLengthQueuingStrategy: ...
    highWaterMark: float
    size: Function

class CountQueuingStrategy:
    @classmethod
    def new(self, init: QueuingStrategyInit) -> CountQueuingStrategy: ...
    highWaterMark: float
    size: Function

class GenericTransformStream:
    readable: ReadableStream
    writable: WritableStream

class TimeEvent(Event):
    view: WindowProxy | None
    detail: int
    def initTimeEvent(self, typeArg: str, viewArg: Window | None, detailArg: int): ...

class SVGAnimationElement(SVGElement, SVGTests):
    targetElement: SVGElement | None
    onbegin: EventHandler
    onend: EventHandler
    onrepeat: EventHandler
    def getStartTime(self) -> float: ...
    def getCurrentTime(self) -> float: ...
    def getSimpleDuration(self) -> float: ...
    def beginElement(self): ...
    def beginElementAt(self, offset: float): ...
    def endElement(self): ...
    def endElementAt(self, offset: float): ...

class SVGAnimateElement(SVGAnimationElement): ...

class SVGSetElement(SVGAnimationElement): ...

class SVGAnimateMotionElement(SVGAnimationElement): ...

class SVGMPathElement(SVGElement, SVGURIReference): ...

class SVGAnimateTransformElement(SVGAnimationElement): ...

class SVGDiscardElement(SVGAnimationElement): ...

class TestutilsNamespace:
    def gc(self) -> Awaitable[None]: ...

class TextDetector:
    @classmethod
    def new(self) -> TextDetector: ...
    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedText]]: ...

class DetectedText(TypedDict):
    boundingBox: DOMRectReadOnly
    rawValue: str
    cornerPoints: Sequence[Point2D]

class TouchInit(TypedDict):
    identifier: int
    target: EventTarget
    clientX: NotRequired[float]
    clientY: NotRequired[float]
    screenX: NotRequired[float]
    screenY: NotRequired[float]
    pageX: NotRequired[float]
    pageY: NotRequired[float]
    radiusX: NotRequired[float]
    radiusY: NotRequired[float]
    rotationAngle: NotRequired[float]
    force: NotRequired[float]
    altitudeAngle: NotRequired[float]
    azimuthAngle: NotRequired[float]
    touchType: NotRequired[TouchType]

class Touch:
    @classmethod
    def new(self, touchInitDict: TouchInit) -> Touch: ...
    identifier: int
    target: EventTarget
    screenX: float
    screenY: float
    clientX: float
    clientY: float
    pageX: float
    pageY: float
    radiusX: float
    radiusY: float
    rotationAngle: float
    force: float
    altitudeAngle: float
    azimuthAngle: float
    touchType: TouchType

class TouchList:
    length: int

class TouchEventInit(TypedDict, EventModifierInit):
    touches: NotRequired[Sequence[Touch]]
    targetTouches: NotRequired[Sequence[Touch]]
    changedTouches: NotRequired[Sequence[Touch]]

class TouchEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: TouchEventInit | None = {}) -> TouchEvent: ...
    touches: TouchList
    targetTouches: TouchList
    changedTouches: TouchList
    altKey: bool
    metaKey: bool
    ctrlKey: bool
    shiftKey: bool

class TrustedHTML:
    def toJSON(self) -> str: ...

class TrustedScript:
    def toJSON(self) -> str: ...

class TrustedScriptURL:
    def toJSON(self) -> USVString: ...

class TrustedTypePolicyFactory:
    def createPolicy(self, policyName: str, policyOptions: TrustedTypePolicyOptions | None = {}) -> TrustedTypePolicy: ...
    def isHTML(self, value: Any) -> bool: ...
    def isScript(self, value: Any) -> bool: ...
    def isScriptURL(self, value: Any) -> bool: ...
    emptyHTML: TrustedHTML
    emptyScript: TrustedScript
    def getAttributeType(self, tagName: str, attribute: str, elementNs: str | None = "", attrNs: str | None = "") -> str | None: ...
    def getPropertyType(self, tagName: str, property: str, elementNs: str | None = "") -> str | None: ...
    defaultPolicy: TrustedTypePolicy | None

class TrustedTypePolicy:
    name: str
    def createHTML(self, input: str, *arguments: Any) -> TrustedHTML: ...
    def createScript(self, input: str, *arguments: Any) -> TrustedScript: ...
    def createScriptURL(self, input: str, *arguments: Any) -> TrustedScriptURL: ...

class TrustedTypePolicyOptions(TypedDict):
    createHTML: NotRequired[CreateHTMLCallback | None]
    createScript: NotRequired[CreateScriptCallback | None]
    createScriptURL: NotRequired[CreateScriptURLCallback | None]

class NavigatorUABrandVersion(TypedDict):
    brand: NotRequired[str]
    version: NotRequired[str]

class UADataValues(TypedDict):
    brands: NotRequired[Sequence[NavigatorUABrandVersion]]
    mobile: NotRequired[bool]
    architecture: NotRequired[str]
    bitness: NotRequired[str]
    model: NotRequired[str]
    platform: NotRequired[str]
    platformVersion: NotRequired[str]
    uaFullVersion: NotRequired[str]
    wow64: NotRequired[bool]
    fullVersionList: NotRequired[Sequence[NavigatorUABrandVersion]]

class UALowEntropyJSON(TypedDict):
    brands: NotRequired[Sequence[NavigatorUABrandVersion]]
    mobile: NotRequired[bool]
    platform: NotRequired[str]

class NavigatorUAData:
    brands: Sequence[NavigatorUABrandVersion]
    mobile: bool
    platform: str
    def getHighEntropyValues(self, hints: Sequence[str]) -> Awaitable[UADataValues]: ...
    def toJSON(self) -> UALowEntropyJSON: ...

class NavigatorUA:
    userAgentData: NavigatorUAData

class FocusEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: FocusEventInit | None = {}) -> FocusEvent: ...
    relatedTarget: EventTarget | None

class FocusEventInit(TypedDict, UIEventInit):
    relatedTarget: NotRequired[EventTarget | None]

class EventModifierInit(TypedDict, UIEventInit):
    ctrlKey: NotRequired[bool]
    shiftKey: NotRequired[bool]
    altKey: NotRequired[bool]
    metaKey: NotRequired[bool]
    modifierAltGraph: NotRequired[bool]
    modifierCapsLock: NotRequired[bool]
    modifierFn: NotRequired[bool]
    modifierFnLock: NotRequired[bool]
    modifierHyper: NotRequired[bool]
    modifierNumLock: NotRequired[bool]
    modifierScrollLock: NotRequired[bool]
    modifierSuper: NotRequired[bool]
    modifierSymbol: NotRequired[bool]
    modifierSymbolLock: NotRequired[bool]

class WheelEvent(MouseEvent):
    @classmethod
    def new(self, type: str, eventInitDict: WheelEventInit | None = {}) -> WheelEvent: ...
    DOM_DELTA_PIXEL = 0x00
    DOM_DELTA_LINE = 0x01
    DOM_DELTA_PAGE = 0x02
    deltaX: float
    deltaY: float
    deltaZ: float
    deltaMode: int

class WheelEventInit(TypedDict, MouseEventInit):
    deltaX: NotRequired[float]
    deltaY: NotRequired[float]
    deltaZ: NotRequired[float]
    deltaMode: NotRequired[int]

class KeyboardEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: KeyboardEventInit | None = {}) -> KeyboardEvent: ...
    DOM_KEY_LOCATION_STANDARD = 0x00
    DOM_KEY_LOCATION_LEFT = 0x01
    DOM_KEY_LOCATION_RIGHT = 0x02
    DOM_KEY_LOCATION_NUMPAD = 0x03
    key: str
    code: str
    location: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    repeat: bool
    isComposing: bool
    def getModifierState(self, keyArg: str) -> bool: ...
    def initKeyboardEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: Window | None = None, keyArg: str | None = "", locationArg: int | None = 0, ctrlKey: bool | None = false, altKey: bool | None = false, shiftKey: bool | None = false, metaKey: bool | None = false): ...
    charCode: int
    keyCode: int

class KeyboardEventInit(TypedDict, EventModifierInit, TypedDict):
    key: NotRequired[str]
    code: NotRequired[str]
    location: NotRequired[int]
    repeat: NotRequired[bool]
    isComposing: NotRequired[bool]
    charCode: NotRequired[int]
    keyCode: NotRequired[int]

class CompositionEvent(UIEvent):
    @classmethod
    def new(self, type: str, eventInitDict: CompositionEventInit | None = {}) -> CompositionEvent: ...
    data: str
    def initCompositionEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: WindowProxy | None = None, dataArg: str | None = ""): ...

class CompositionEventInit(TypedDict, UIEventInit):
    data: NotRequired[str]

class MutationEvent(Event):
    MODIFICATION = 1
    ADDITION = 2
    REMOVAL = 3
    relatedNode: Node | None
    prevValue: str
    newValue: str
    attrName: str
    attrChange: int
    def initMutationEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, relatedNodeArg: Node | None = None, prevValueArg: str | None = "", newValueArg: str | None = "", attrNameArg: str | None = "", attrChangeArg: int | None = 0): ...

class URLSearchParams:
    @classmethod
    def new(self, init: Sequence[Sequence[USVString]] | USVString | USVString | None = "") -> URLSearchParams: ...
    def append(self, name: USVString, value: USVString): ...
    def delete(self, name: USVString): ...
    def get(self, name: USVString) -> USVString | None: ...
    def getAll(self, name: USVString) -> Sequence[USVString]: ...
    def has(self, name: USVString) -> bool: ...
    def set(self, name: USVString, value: USVString): ...
    def sort(self): ...

class URLPattern:
    @overload
    @classmethod
    def new(self, input: URLPatternInput, baseURL: USVString, options: URLPatternOptions | None = {}) -> URLPattern: ...
    @overload
    @classmethod
    def new(self, input: URLPatternInput | None = {}, options: URLPatternOptions | None = {}) -> URLPattern: ...
    def test(self, input: URLPatternInput | None = {}, baseURL: USVString | None = None) -> bool: ...
    def exec(self, input: URLPatternInput | None = {}, baseURL: USVString | None = None) -> URLPatternResult | None: ...
    protocol: USVString
    username: USVString
    password: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class URLPatternInit(TypedDict):
    protocol: NotRequired[USVString]
    username: NotRequired[USVString]
    password: NotRequired[USVString]
    hostname: NotRequired[USVString]
    port: NotRequired[USVString]
    pathname: NotRequired[USVString]
    search: NotRequired[USVString]
    hash: NotRequired[USVString]
    baseURL: NotRequired[USVString]

class URLPatternOptions(TypedDict):
    ignoreCase: NotRequired[bool]

class URLPatternResult(TypedDict):
    inputs: NotRequired[Sequence[URLPatternInput]]
    protocol: NotRequired[URLPatternComponentResult]
    username: NotRequired[URLPatternComponentResult]
    password: NotRequired[URLPatternComponentResult]
    hostname: NotRequired[URLPatternComponentResult]
    port: NotRequired[URLPatternComponentResult]
    pathname: NotRequired[URLPatternComponentResult]
    search: NotRequired[URLPatternComponentResult]
    hash: NotRequired[URLPatternComponentResult]

class URLPatternComponentResult(TypedDict):
    input: NotRequired[USVString]
    groups: NotRequired[USVString | None]

class PerformanceMarkOptions(TypedDict):
    detail: NotRequired[Any]
    startTime: NotRequired[DOMHighResTimeStamp]

class PerformanceMeasureOptions(TypedDict):
    detail: NotRequired[Any]
    start: NotRequired[str | DOMHighResTimeStamp]
    duration: NotRequired[DOMHighResTimeStamp]
    end: NotRequired[str | DOMHighResTimeStamp]

class PerformanceMark(PerformanceEntry):
    @classmethod
    def new(self, markName: str, markOptions: PerformanceMarkOptions | None = {}) -> PerformanceMark: ...
    detail: Any

class PerformanceMeasure(PerformanceEntry):
    detail: Any

class VideoFrameCallbackMetadata(TypedDict):
    presentationTime: DOMHighResTimeStamp
    expectedDisplayTime: DOMHighResTimeStamp
    width: int
    height: int
    mediaTime: float
    presentedFrames: int
    processingDuration: NotRequired[float]
    captureTime: NotRequired[DOMHighResTimeStamp]
    receiveTime: NotRequired[DOMHighResTimeStamp]
    rtpTimestamp: NotRequired[int]

class VirtualKeyboard(EventTarget):
    def show(self): ...
    def hide(self): ...
    boundingRect: DOMRect
    overlaysContent: bool
    ongeometrychange: EventHandler

class ARIAMixin:
    role: str | None
    ariaActiveDescendantElement: Element | None
    ariaAtomic: str | None
    ariaAutoComplete: str | None
    ariaBusy: str | None
    ariaChecked: str | None
    ariaColCount: str | None
    ariaColIndex: str | None
    ariaColIndexText: str | None
    ariaColSpan: str | None
    ariaControlsElements: Sequence[Element]
    ariaCurrent: str | None
    ariaDescribedByElements: Sequence[Element]
    ariaDescription: str | None
    ariaDetailsElements: Sequence[Element]
    ariaDisabled: str | None
    ariaErrorMessageElements: Sequence[Element]
    ariaExpanded: str | None
    ariaFlowToElements: Sequence[Element]
    ariaHasPopup: str | None
    ariaHidden: str | None
    ariaInvalid: str | None
    ariaKeyShortcuts: str | None
    ariaLabel: str | None
    ariaLabelledByElements: Sequence[Element]
    ariaLevel: str | None
    ariaLive: str | None
    ariaModal: str | None
    ariaMultiLine: str | None
    ariaMultiSelectable: str | None
    ariaOrientation: str | None
    ariaOwnsElements: Sequence[Element]
    ariaPlaceholder: str | None
    ariaPosInSet: str | None
    ariaPressed: str | None
    ariaReadOnly: str | None
    ariaRequired: str | None
    ariaRoleDescription: str | None
    ariaRowCount: str | None
    ariaRowIndex: str | None
    ariaRowIndexText: str | None
    ariaRowSpan: str | None
    ariaSelected: str | None
    ariaSetSize: str | None
    ariaSort: str | None
    ariaValueMax: str | None
    ariaValueMin: str | None
    ariaValueNow: str | None
    ariaValueText: str | None

class WebAssemblyInstantiatedSource(TypedDict):
    module: Module
    instance: Instance

class WebassemblyNamespace:
    def validate(self, bytes: BufferSource) -> bool: ...
    def compile(self, bytes: BufferSource) -> Awaitable[Module]: ...
    @overload
    def instantiate(self, bytes: BufferSource, importObject: object | None = None) -> Awaitable[WebAssemblyInstantiatedSource]: ...
    @overload
    def instantiate(self, moduleObject: Module, importObject: object | None = None) -> Awaitable[Instance]: ...
    def compileStreaming(self, source: Awaitable[Response]) -> Awaitable[Module]: ...
    def instantiateStreaming(self, source: Awaitable[Response], importObject: object | None = None) -> Awaitable[WebAssemblyInstantiatedSource]: ...

class ModuleExportDescriptor(TypedDict):
    name: USVString
    kind: ImportExportKind

class ModuleImportDescriptor(TypedDict):
    module: USVString
    name: USVString
    kind: ImportExportKind

class Module:
    @classmethod
    def new(self, bytes: BufferSource) -> Module: ...

class Instance:
    @classmethod
    def new(self, module: Module, importObject: object | None = None) -> Instance: ...
    exports: object

class MemoryDescriptor(TypedDict):
    initial: int
    maximum: NotRequired[int]

class Memory:
    @classmethod
    def new(self, descriptor: MemoryDescriptor) -> Memory: ...
    def grow(self, delta: int) -> int: ...
    buffer: ArrayBuffer

class TableDescriptor(TypedDict):
    element: TableKind
    initial: int
    maximum: NotRequired[int]

class Table:
    @classmethod
    def new(self, descriptor: TableDescriptor, value: Any | None = None) -> Table: ...
    def grow(self, delta: int, value: Any | None = None) -> int: ...
    def get(self, index: int) -> Any: ...
    def set(self, index: int, value: Any | None = None): ...
    length: int

class GlobalDescriptor(TypedDict):
    value: ValueType
    mutable: NotRequired[bool]

class Global:
    @classmethod
    def new(self, descriptor: GlobalDescriptor, v: Any | None = None) -> Global: ...
    def valueOf(self) -> Any: ...
    value: Any

class Animation(EventTarget):
    @classmethod
    def new(self, effect: AnimationEffect | None = None, timeline: AnimationTimeline | None = None) -> Animation: ...
    startTime: CSSNumberish | None
    currentTime: CSSNumberish | None
    id: str
    effect: AnimationEffect | None
    timeline: AnimationTimeline | None
    playbackRate: float
    playState: AnimationPlayState
    replaceState: AnimationReplaceState
    pending: bool
    ready: Awaitable[Animation]
    finished: Awaitable[Animation]
    onfinish: EventHandler
    oncancel: EventHandler
    onremove: EventHandler
    def cancel(self): ...
    def finish(self): ...
    def play(self): ...
    def pause(self): ...
    def updatePlaybackRate(self, playbackRate: float): ...
    def reverse(self): ...
    def persist(self): ...
    def commitStyles(self): ...

class AnimationEffect:
    parent: GroupEffect | None
    previousSibling: AnimationEffect | None
    nextSibling: AnimationEffect | None
    def before(self, *effects: AnimationEffect): ...
    def after(self, *effects: AnimationEffect): ...
    def replace(self, *effects: AnimationEffect): ...
    def remove(self): ...
    def getTiming(self) -> EffectTiming: ...
    def getComputedTiming(self) -> ComputedEffectTiming: ...
    def updateTiming(self, timing: OptionalEffectTiming | None = {}): ...

class EffectTiming(TypedDict, TypedDict):
    delay: NotRequired[float]
    endDelay: NotRequired[float]
    playbackRate: NotRequired[float]
    duration: NotRequired[float | CSSNumericValue | str]
    fill: NotRequired[FillMode]
    iterationStart: NotRequired[float]
    iterations: NotRequired[float]
    direction: NotRequired[PlaybackDirection]
    easing: NotRequired[str]

class OptionalEffectTiming(TypedDict, TypedDict):
    playbackRate: NotRequired[float]
    delay: NotRequired[float]
    endDelay: NotRequired[float]
    fill: NotRequired[FillMode]
    iterationStart: NotRequired[float]
    iterations: NotRequired[float]
    duration: NotRequired[float | str]
    direction: NotRequired[PlaybackDirection]
    easing: NotRequired[str]

class ComputedEffectTiming(TypedDict, TypedDict, EffectTiming):
    startTime: NotRequired[CSSNumberish]
    endTime: NotRequired[CSSNumberish]
    activeDuration: NotRequired[CSSNumberish]
    localTime: NotRequired[CSSNumberish | None]
    progress: NotRequired[float | None]
    currentIteration: NotRequired[float | None]

class GroupEffect:
    @classmethod
    def new(self, children: Sequence[AnimationEffect], timing: float | EffectTiming | None = {}) -> GroupEffect: ...
    children: AnimationNodeList
    firstChild: AnimationEffect | None
    lastChild: AnimationEffect | None
    def clone(self) -> GroupEffect: ...
    def prepend(self, *effects: AnimationEffect): ...
    def append(self, *effects: AnimationEffect): ...

class AnimationNodeList:
    length: int

class SequenceEffect(GroupEffect):
    @classmethod
    def new(self, children: Sequence[AnimationEffect], timing: float | EffectTiming | None = {}) -> SequenceEffect: ...
    def clone(self) -> SequenceEffect: ...

class KeyframeEffect(AnimationEffect):
    @overload
    @classmethod
    def new(self, target: Element | None, keyframes: object | None, options: float | KeyframeEffectOptions | None = {}) -> KeyframeEffect: ...
    @overload
    @classmethod
    def new(self, source: KeyframeEffect) -> KeyframeEffect: ...
    iterationComposite: IterationCompositeOperation
    target: Element | None
    pseudoElement: CSSOMString | None
    composite: CompositeOperation
    def getKeyframes(self) -> Sequence[object]: ...
    def setKeyframes(self, keyframes: object | None): ...

class KeyframeEffectOptions(TypedDict, TypedDict, EffectTiming):
    iterationComposite: NotRequired[IterationCompositeOperation]
    composite: NotRequired[CompositeOperation]
    pseudoElement: NotRequired[CSSOMString | None]

class AnimationPlaybackEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: AnimationPlaybackEventInit | None = {}) -> AnimationPlaybackEvent: ...
    currentTime: CSSNumberish | None
    timelineTime: CSSNumberish | None

class AnimationPlaybackEventInit(TypedDict, EventInit):
    currentTime: NotRequired[CSSNumberish | None]
    timelineTime: NotRequired[CSSNumberish | None]

class DocumentTimelineOptions(TypedDict):
    originTime: NotRequired[DOMHighResTimeStamp]

class DocumentTimeline(AnimationTimeline):
    @classmethod
    def new(self, options: DocumentTimelineOptions | None = {}) -> DocumentTimeline: ...

class BaseComputedKeyframe(TypedDict):
    offset: NotRequired[float | None]
    computedOffset: NotRequired[float]
    easing: NotRequired[str]
    composite: NotRequired[CompositeOperationOrAuto]

class BasePropertyIndexedKeyframe(TypedDict):
    offset: NotRequired[float | None | Sequence[float | None]]
    easing: NotRequired[str | Sequence[str]]
    composite: NotRequired[CompositeOperationOrAuto | Sequence[CompositeOperationOrAuto]]

class BaseKeyframe(TypedDict):
    offset: NotRequired[float | None]
    easing: NotRequired[str]
    composite: NotRequired[CompositeOperationOrAuto]

class Animatable:
    def animate(self, keyframes: object | None, options: float | KeyframeAnimationOptions | None = {}) -> Animation: ...
    def getAnimations(self, options: GetAnimationsOptions | None = {}) -> Sequence[Animation]: ...

class KeyframeAnimationOptions(TypedDict, KeyframeEffectOptions):
    id: NotRequired[str]
    timeline: NotRequired[AnimationTimeline | None]

class GetAnimationsOptions(TypedDict):
    subtree: NotRequired[bool]

class LaunchParams:
    targetURL: str | None
    files: Sequence[FileSystemHandle]

class LaunchQueue:
    def setConsumer(self, consumer: LaunchConsumer): ...

class BluetoothDataFilterInit(TypedDict):
    dataPrefix: NotRequired[BufferSource]
    mask: NotRequired[BufferSource]

class BluetoothManufacturerDataFilterInit(TypedDict, BluetoothDataFilterInit):
    companyIdentifier: int

class BluetoothServiceDataFilterInit(TypedDict, BluetoothDataFilterInit):
    service: BluetoothServiceUUID

class BluetoothLEScanFilterInit(TypedDict):
    services: NotRequired[Sequence[BluetoothServiceUUID]]
    name: NotRequired[str]
    namePrefix: NotRequired[str]
    manufacturerData: NotRequired[Sequence[BluetoothManufacturerDataFilterInit]]
    serviceData: NotRequired[Sequence[BluetoothServiceDataFilterInit]]

class RequestDeviceOptions(TypedDict):
    filters: NotRequired[Sequence[BluetoothLEScanFilterInit]]
    optionalServices: NotRequired[Sequence[BluetoothServiceUUID]]
    optionalManufacturerData: NotRequired[Sequence[int]]
    acceptAllDevices: NotRequired[bool]

class Bluetooth(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    def getAvailability(self) -> Awaitable[bool]: ...
    onavailabilitychanged: EventHandler
    referringDevice: BluetoothDevice | None
    def getDevices(self) -> Awaitable[Sequence[BluetoothDevice]]: ...
    def requestDevice(self, options: RequestDeviceOptions | None = {}) -> Awaitable[BluetoothDevice]: ...

class BluetoothPermissionDescriptor(TypedDict, PermissionDescriptor):
    deviceId: NotRequired[str]
    filters: NotRequired[Sequence[BluetoothLEScanFilterInit]]
    optionalServices: NotRequired[Sequence[BluetoothServiceUUID]]
    optionalManufacturerData: NotRequired[Sequence[int]]
    acceptAllDevices: NotRequired[bool]

class AllowedBluetoothDevice(TypedDict):
    deviceId: str
    mayUseGATT: bool
    allowedServices: str | Sequence[UUID]
    allowedManufacturerData: Sequence[int]

class BluetoothPermissionStorage(TypedDict):
    allowedDevices: Sequence[AllowedBluetoothDevice]

class BluetoothPermissionResult(PermissionStatus):
    devices: Sequence[BluetoothDevice]

class ValueEvent(Event):
    @classmethod
    def new(self, type: str, initDict: ValueEventInit | None = {}) -> ValueEvent: ...
    value: Any

class ValueEventInit(TypedDict, EventInit):
    value: NotRequired[Any]

class BluetoothDevice(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    id: str
    name: str | None
    gatt: BluetoothRemoteGATTServer | None
    def forget(self) -> Awaitable[None]: ...
    def watchAdvertisements(self, options: WatchAdvertisementsOptions | None = {}) -> Awaitable[None]: ...
    watchingAdvertisements: bool

class WatchAdvertisementsOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class BluetoothManufacturerDataMap: ...

class BluetoothServiceDataMap: ...

class BluetoothAdvertisingEvent(Event):
    @classmethod
    def new(self, type: str, init: BluetoothAdvertisingEventInit) -> BluetoothAdvertisingEvent: ...
    device: BluetoothDevice
    uuids: Sequence[UUID]
    name: str | None
    appearance: int | None
    txPower: byte | None
    rssi: byte | None
    manufacturerData: BluetoothManufacturerDataMap
    serviceData: BluetoothServiceDataMap

class BluetoothAdvertisingEventInit(TypedDict, EventInit):
    device: BluetoothDevice
    uuids: NotRequired[Sequence[str | int]]
    name: NotRequired[str]
    appearance: NotRequired[int]
    txPower: NotRequired[byte]
    rssi: NotRequired[byte]
    manufacturerData: NotRequired[BluetoothManufacturerDataMap]
    serviceData: NotRequired[BluetoothServiceDataMap]

class BluetoothRemoteGATTServer:
    device: BluetoothDevice
    connected: bool
    def connect(self) -> Awaitable[BluetoothRemoteGATTServer]: ...
    def disconnect(self): ...
    def getPrimaryService(self, service: BluetoothServiceUUID) -> Awaitable[BluetoothRemoteGATTService]: ...
    def getPrimaryServices(self, service: BluetoothServiceUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTService]]: ...

class BluetoothRemoteGATTService(EventTarget, CharacteristicEventHandlers, ServiceEventHandlers):
    device: BluetoothDevice
    uuid: UUID
    isPrimary: bool
    def getCharacteristic(self, characteristic: BluetoothCharacteristicUUID) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...
    def getCharacteristics(self, characteristic: BluetoothCharacteristicUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTCharacteristic]]: ...
    def getIncludedService(self, service: BluetoothServiceUUID) -> Awaitable[BluetoothRemoteGATTService]: ...
    def getIncludedServices(self, service: BluetoothServiceUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTService]]: ...

class BluetoothRemoteGATTCharacteristic(EventTarget, CharacteristicEventHandlers):
    service: BluetoothRemoteGATTService
    uuid: UUID
    properties: BluetoothCharacteristicProperties
    value: DataView
    def getDescriptor(self, descriptor: BluetoothDescriptorUUID) -> Awaitable[BluetoothRemoteGATTDescriptor]: ...
    def getDescriptors(self, descriptor: BluetoothDescriptorUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTDescriptor]]: ...
    def readValue(self) -> Awaitable[DataView]: ...
    def writeValue(self, value: BufferSource) -> Awaitable[None]: ...
    def writeValueWithResponse(self, value: BufferSource) -> Awaitable[None]: ...
    def writeValueWithoutResponse(self, value: BufferSource) -> Awaitable[None]: ...
    def startNotifications(self) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...
    def stopNotifications(self) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...

class BluetoothCharacteristicProperties:
    broadcast: bool
    read: bool
    writeWithoutResponse: bool
    write: bool
    notify: bool
    indicate: bool
    authenticatedSignedWrites: bool
    reliableWrite: bool
    writableAuxiliaries: bool

class BluetoothRemoteGATTDescriptor:
    characteristic: BluetoothRemoteGATTCharacteristic
    uuid: UUID
    value: DataView
    def readValue(self) -> Awaitable[DataView]: ...
    def writeValue(self, value: BufferSource) -> Awaitable[None]: ...

class CharacteristicEventHandlers:
    oncharacteristicvaluechanged: EventHandler

class BluetoothDeviceEventHandlers:
    onadvertisementreceived: EventHandler
    ongattserverdisconnected: EventHandler

class ServiceEventHandlers:
    onserviceadded: EventHandler
    onservicechanged: EventHandler
    onserviceremoved: EventHandler

class BluetoothUUID: ...

class NavigatorLocks:
    locks: LockManager

class LockManager:
    @overload
    def request(self, name: str, callback: LockGrantedCallback) -> Awaitable[Any]: ...
    @overload
    def request(self, name: str, options: LockOptions, callback: LockGrantedCallback) -> Awaitable[Any]: ...
    def query(self) -> Awaitable[LockManagerSnapshot]: ...

class LockOptions(TypedDict):
    mode: NotRequired[LockMode]
    ifAvailable: NotRequired[bool]
    steal: NotRequired[bool]
    signal: NotRequired[AbortSignal]

class LockManagerSnapshot(TypedDict):
    held: NotRequired[Sequence[LockInfo]]
    pending: NotRequired[Sequence[LockInfo]]

class LockInfo(TypedDict):
    name: NotRequired[str]
    mode: NotRequired[LockMode]
    clientId: NotRequired[str]

class Lock:
    name: str
    mode: LockMode

class NDEFMessage:
    @classmethod
    def new(self, messageInit: NDEFMessageInit) -> NDEFMessage: ...
    records: Sequence[NDEFRecord]

class NDEFMessageInit(TypedDict):
    records: Sequence[NDEFRecordInit]

class NDEFRecord:
    @classmethod
    def new(self, recordInit: NDEFRecordInit) -> NDEFRecord: ...
    recordType: USVString
    mediaType: USVString | None
    id: USVString | None
    data: DataView
    encoding: USVString | None
    lang: USVString | None
    def toRecords(self) -> Sequence[NDEFRecord]: ...

class NDEFRecordInit(TypedDict):
    recordType: USVString
    mediaType: NotRequired[USVString]
    id: NotRequired[USVString]
    encoding: NotRequired[USVString]
    lang: NotRequired[USVString]
    data: NotRequired[Any]

class NDEFReader(EventTarget):
    @classmethod
    def new(self) -> NDEFReader: ...
    onreading: EventHandler
    onreadingerror: EventHandler
    def scan(self, options: NDEFScanOptions | None = {}) -> Awaitable[None]: ...
    def write(self, message: NDEFMessageSource, options: NDEFWriteOptions | None = {}) -> Awaitable[None]: ...
    def makeReadOnly(self, options: NDEFMakeReadOnlyOptions | None = {}) -> Awaitable[None]: ...

class NDEFReadingEvent(Event):
    @classmethod
    def new(self, type: str, readingEventInitDict: NDEFReadingEventInit) -> NDEFReadingEvent: ...
    serialNumber: str
    message: NDEFMessage

class NDEFReadingEventInit(TypedDict, EventInit):
    serialNumber: NotRequired[str | None]
    message: NDEFMessageInit

class NDEFWriteOptions(TypedDict):
    overwrite: NotRequired[bool]
    signal: NotRequired[AbortSignal | None]

class NDEFMakeReadOnlyOptions(TypedDict):
    signal: NotRequired[AbortSignal | None]

class NDEFScanOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class OTPCredential(Credential):
    code: str

class OTPCredentialRequestOptions(TypedDict):
    transport: NotRequired[Sequence[OTPCredentialTransportType]]

class ShareData(TypedDict):
    files: NotRequired[Sequence[File]]
    title: NotRequired[USVString]
    text: NotRequired[USVString]
    url: NotRequired[USVString]

class BaseAudioContext(EventTarget):
    destination: AudioDestinationNode
    sampleRate: float
    currentTime: float
    listener: AudioListener
    state: AudioContextState
    audioWorklet: AudioWorklet
    onstatechange: EventHandler
    def createAnalyser(self) -> AnalyserNode: ...
    def createBiquadFilter(self) -> BiquadFilterNode: ...
    def createBuffer(self, numberOfChannels: int, length: int, sampleRate: float) -> AudioBuffer: ...
    def createBufferSource(self) -> AudioBufferSourceNode: ...
    def createChannelMerger(self, numberOfInputs: int | None = 6) -> ChannelMergerNode: ...
    def createChannelSplitter(self, numberOfOutputs: int | None = 6) -> ChannelSplitterNode: ...
    def createConstantSource(self) -> ConstantSourceNode: ...
    def createConvolver(self) -> ConvolverNode: ...
    def createDelay(self, maxDelayTime: float | None = 1.0) -> DelayNode: ...
    def createDynamicsCompressor(self) -> DynamicsCompressorNode: ...
    def createGain(self) -> GainNode: ...
    def createIIRFilter(self, feedforward: Sequence[float], feedback: Sequence[float]) -> IIRFilterNode: ...
    def createOscillator(self) -> OscillatorNode: ...
    def createPanner(self) -> PannerNode: ...
    def createPeriodicWave(self, real: Sequence[float], imag: Sequence[float], constraints: PeriodicWaveConstraints | None = {}) -> PeriodicWave: ...
    def createScriptProcessor(self, bufferSize: int | None = 0, numberOfInputChannels: int | None = 2, numberOfOutputChannels: int | None = 2) -> ScriptProcessorNode: ...
    def createStereoPanner(self) -> StereoPannerNode: ...
    def createWaveShaper(self) -> WaveShaperNode: ...
    def decodeAudioData(self, audioData: ArrayBuffer, successCallback: DecodeSuccessCallback | None = None, errorCallback: DecodeErrorCallback | None = None) -> Awaitable[AudioBuffer]: ...

class AudioContext(BaseAudioContext):
    @classmethod
    def new(self, contextOptions: AudioContextOptions | None = {}) -> AudioContext: ...
    baseLatency: float
    outputLatency: float
    sinkId: str | AudioSinkInfo
    renderCapacity: AudioRenderCapacity
    onsinkchange: EventHandler
    def getOutputTimestamp(self) -> AudioTimestamp: ...
    def resume(self) -> Awaitable[None]: ...
    def suspend(self) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def setSinkId(self, sinkId: str | AudioSinkOptions) -> Awaitable[None]: ...
    def createMediaElementSource(self, mediaElement: HTMLMediaElement) -> MediaElementAudioSourceNode: ...
    def createMediaStreamSource(self, mediaStream: MediaStream) -> MediaStreamAudioSourceNode: ...
    def createMediaStreamTrackSource(self, mediaStreamTrack: MediaStreamTrack) -> MediaStreamTrackAudioSourceNode: ...
    def createMediaStreamDestination(self) -> MediaStreamAudioDestinationNode: ...

class AudioContextOptions(TypedDict):
    latencyHint: NotRequired[AudioContextLatencyCategory | float]
    sampleRate: NotRequired[float]
    sinkId: NotRequired[str | AudioSinkOptions]

class AudioSinkOptions(TypedDict):
    type: AudioSinkType

class AudioSinkInfo:
    type: AudioSinkType

class AudioTimestamp(TypedDict):
    contextTime: NotRequired[float]
    performanceTime: NotRequired[DOMHighResTimeStamp]

class AudioRenderCapacity(EventTarget):
    def start(self, options: AudioRenderCapacityOptions | None = {}): ...
    def stop(self): ...
    onupdate: EventHandler

class AudioRenderCapacityOptions(TypedDict):
    updateInterval: NotRequired[float]

class AudioRenderCapacityEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: AudioRenderCapacityEventInit | None = {}) -> AudioRenderCapacityEvent: ...
    timestamp: float
    averageLoad: float
    peakLoad: float
    underrunRatio: float

class AudioRenderCapacityEventInit(TypedDict, EventInit):
    timestamp: NotRequired[float]
    averageLoad: NotRequired[float]
    peakLoad: NotRequired[float]
    underrunRatio: NotRequired[float]

class OfflineAudioContext(BaseAudioContext):
    @overload
    @classmethod
    def new(self, contextOptions: OfflineAudioContextOptions) -> OfflineAudioContext: ...
    @overload
    @classmethod
    def new(self, numberOfChannels: int, length: int, sampleRate: float) -> OfflineAudioContext: ...
    def startRendering(self) -> Awaitable[AudioBuffer]: ...
    def resume(self) -> Awaitable[None]: ...
    def suspend(self, suspendTime: float) -> Awaitable[None]: ...
    length: int
    oncomplete: EventHandler

class OfflineAudioContextOptions(TypedDict):
    numberOfChannels: NotRequired[int]
    length: int
    sampleRate: float

class OfflineAudioCompletionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: OfflineAudioCompletionEventInit) -> OfflineAudioCompletionEvent: ...
    renderedBuffer: AudioBuffer

class OfflineAudioCompletionEventInit(TypedDict, EventInit):
    renderedBuffer: AudioBuffer

class AudioBuffer:
    @classmethod
    def new(self, options: AudioBufferOptions) -> AudioBuffer: ...
    sampleRate: float
    length: int
    duration: float
    numberOfChannels: int
    def getChannelData(self, channel: int) -> Float32Array: ...
    def copyFromChannel(self, destination: Float32Array, channelNumber: int, bufferOffset: int | None = 0): ...
    def copyToChannel(self, source: Float32Array, channelNumber: int, bufferOffset: int | None = 0): ...

class AudioBufferOptions(TypedDict):
    numberOfChannels: NotRequired[int]
    length: int
    sampleRate: float

class AudioNode(EventTarget):
    @overload
    def connect(self, destinationNode: AudioNode, output: int | None = 0, input: int | None = 0) -> AudioNode: ...
    @overload
    def connect(self, destinationParam: AudioParam, output: int | None = 0): ...
    @overload
    def disconnect(self): ...
    @overload
    def disconnect(self, output: int): ...
    @overload
    def disconnect(self, destinationNode: AudioNode): ...
    @overload
    def disconnect(self, destinationNode: AudioNode, output: int): ...
    @overload
    def disconnect(self, destinationNode: AudioNode, output: int, input: int): ...
    @overload
    def disconnect(self, destinationParam: AudioParam): ...
    @overload
    def disconnect(self, destinationParam: AudioParam, output: int): ...
    context: BaseAudioContext
    numberOfInputs: int
    numberOfOutputs: int
    channelCount: int
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation

class AudioNodeOptions(TypedDict):
    channelCount: NotRequired[int]
    channelCountMode: NotRequired[ChannelCountMode]
    channelInterpretation: NotRequired[ChannelInterpretation]

class AudioParam:
    value: float
    automationRate: AutomationRate
    defaultValue: float
    minValue: float
    maxValue: float
    def setValueAtTime(self, value: float, startTime: float) -> AudioParam: ...
    def linearRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...
    def exponentialRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...
    def setTargetAtTime(self, target: float, startTime: float, timeConstant: float) -> AudioParam: ...
    def setValueCurveAtTime(self, values: Sequence[float], startTime: float, duration: float) -> AudioParam: ...
    def cancelScheduledValues(self, cancelTime: float) -> AudioParam: ...
    def cancelAndHoldAtTime(self, cancelTime: float) -> AudioParam: ...

class AudioScheduledSourceNode(AudioNode):
    onended: EventHandler
    def start(self, when: float | None = 0): ...
    def stop(self, when: float | None = 0): ...

class AnalyserNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: AnalyserOptions | None = {}) -> AnalyserNode: ...
    def getFloatFrequencyData(self, array: Float32Array): ...
    def getByteFrequencyData(self, array: Uint8Array): ...
    def getFloatTimeDomainData(self, array: Float32Array): ...
    def getByteTimeDomainData(self, array: Uint8Array): ...
    fftSize: int
    frequencyBinCount: int
    minDecibels: float
    maxDecibels: float
    smoothingTimeConstant: float

class AnalyserOptions(TypedDict, AudioNodeOptions):
    fftSize: NotRequired[int]
    maxDecibels: NotRequired[float]
    minDecibels: NotRequired[float]
    smoothingTimeConstant: NotRequired[float]

class AudioBufferSourceNode(AudioScheduledSourceNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: AudioBufferSourceOptions | None = {}) -> AudioBufferSourceNode: ...
    buffer: AudioBuffer | None
    playbackRate: AudioParam
    detune: AudioParam
    loop: bool
    loopStart: float
    loopEnd: float
    def start(self, when: float | None = 0, offset: float | None = None, duration: float | None = None): ...

class AudioBufferSourceOptions(TypedDict):
    buffer: NotRequired[AudioBuffer | None]
    detune: NotRequired[float]
    loop: NotRequired[bool]
    loopEnd: NotRequired[float]
    loopStart: NotRequired[float]
    playbackRate: NotRequired[float]

class AudioDestinationNode(AudioNode):
    maxChannelCount: int

class AudioListener:
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    forwardX: AudioParam
    forwardY: AudioParam
    forwardZ: AudioParam
    upX: AudioParam
    upY: AudioParam
    upZ: AudioParam
    def setPosition(self, x: float, y: float, z: float): ...
    def setOrientation(self, x: float, y: float, z: float, xUp: float, yUp: float, zUp: float): ...

class AudioProcessingEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: AudioProcessingEventInit) -> AudioProcessingEvent: ...
    playbackTime: float
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer

class AudioProcessingEventInit(TypedDict, EventInit):
    playbackTime: float
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer

class BiquadFilterNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: BiquadFilterOptions | None = {}) -> BiquadFilterNode: ...
    type: BiquadFilterType
    frequency: AudioParam
    detune: AudioParam
    Q: AudioParam
    gain: AudioParam
    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array, phaseResponse: Float32Array): ...

class BiquadFilterOptions(TypedDict, AudioNodeOptions):
    type: NotRequired[BiquadFilterType]
    Q: NotRequired[float]
    detune: NotRequired[float]
    frequency: NotRequired[float]
    gain: NotRequired[float]

class ChannelMergerNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: ChannelMergerOptions | None = {}) -> ChannelMergerNode: ...

class ChannelMergerOptions(TypedDict, AudioNodeOptions):
    numberOfInputs: NotRequired[int]

class ChannelSplitterNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: ChannelSplitterOptions | None = {}) -> ChannelSplitterNode: ...

class ChannelSplitterOptions(TypedDict, AudioNodeOptions):
    numberOfOutputs: NotRequired[int]

class ConstantSourceNode(AudioScheduledSourceNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: ConstantSourceOptions | None = {}) -> ConstantSourceNode: ...
    offset: AudioParam

class ConstantSourceOptions(TypedDict):
    offset: NotRequired[float]

class ConvolverNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: ConvolverOptions | None = {}) -> ConvolverNode: ...
    buffer: AudioBuffer | None
    normalize: bool

class ConvolverOptions(TypedDict, AudioNodeOptions):
    buffer: NotRequired[AudioBuffer | None]
    disableNormalization: NotRequired[bool]

class DelayNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: DelayOptions | None = {}) -> DelayNode: ...
    delayTime: AudioParam

class DelayOptions(TypedDict, AudioNodeOptions):
    maxDelayTime: NotRequired[float]
    delayTime: NotRequired[float]

class DynamicsCompressorNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: DynamicsCompressorOptions | None = {}) -> DynamicsCompressorNode: ...
    threshold: AudioParam
    knee: AudioParam
    ratio: AudioParam
    reduction: float
    attack: AudioParam
    release: AudioParam

class DynamicsCompressorOptions(TypedDict, AudioNodeOptions):
    attack: NotRequired[float]
    knee: NotRequired[float]
    ratio: NotRequired[float]
    release: NotRequired[float]
    threshold: NotRequired[float]

class GainNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: GainOptions | None = {}) -> GainNode: ...
    gain: AudioParam

class GainOptions(TypedDict, AudioNodeOptions):
    gain: NotRequired[float]

class IIRFilterNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: IIRFilterOptions) -> IIRFilterNode: ...
    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array, phaseResponse: Float32Array): ...

class IIRFilterOptions(TypedDict, AudioNodeOptions):
    feedforward: Sequence[float]
    feedback: Sequence[float]

class MediaElementAudioSourceNode(AudioNode):
    @classmethod
    def new(self, context: AudioContext, options: MediaElementAudioSourceOptions) -> MediaElementAudioSourceNode: ...
    mediaElement: HTMLMediaElement

class MediaElementAudioSourceOptions(TypedDict):
    mediaElement: HTMLMediaElement

class MediaStreamAudioDestinationNode(AudioNode):
    @classmethod
    def new(self, context: AudioContext, options: AudioNodeOptions | None = {}) -> MediaStreamAudioDestinationNode: ...
    stream: MediaStream

class MediaStreamAudioSourceNode(AudioNode):
    @classmethod
    def new(self, context: AudioContext, options: MediaStreamAudioSourceOptions) -> MediaStreamAudioSourceNode: ...
    mediaStream: MediaStream

class MediaStreamAudioSourceOptions(TypedDict):
    mediaStream: MediaStream

class MediaStreamTrackAudioSourceNode(AudioNode):
    @classmethod
    def new(self, context: AudioContext, options: MediaStreamTrackAudioSourceOptions) -> MediaStreamTrackAudioSourceNode: ...

class MediaStreamTrackAudioSourceOptions(TypedDict):
    mediaStreamTrack: MediaStreamTrack

class OscillatorNode(AudioScheduledSourceNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: OscillatorOptions | None = {}) -> OscillatorNode: ...
    type: OscillatorType
    frequency: AudioParam
    detune: AudioParam
    def setPeriodicWave(self, periodicWave: PeriodicWave): ...

class OscillatorOptions(TypedDict, AudioNodeOptions):
    type: NotRequired[OscillatorType]
    frequency: NotRequired[float]
    detune: NotRequired[float]
    periodicWave: NotRequired[PeriodicWave]

class PannerNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: PannerOptions | None = {}) -> PannerNode: ...
    panningModel: PanningModelType
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    orientationX: AudioParam
    orientationY: AudioParam
    orientationZ: AudioParam
    distanceModel: DistanceModelType
    refDistance: float
    maxDistance: float
    rolloffFactor: float
    coneInnerAngle: float
    coneOuterAngle: float
    coneOuterGain: float
    def setPosition(self, x: float, y: float, z: float): ...
    def setOrientation(self, x: float, y: float, z: float): ...

class PannerOptions(TypedDict, AudioNodeOptions):
    panningModel: NotRequired[PanningModelType]
    distanceModel: NotRequired[DistanceModelType]
    positionX: NotRequired[float]
    positionY: NotRequired[float]
    positionZ: NotRequired[float]
    orientationX: NotRequired[float]
    orientationY: NotRequired[float]
    orientationZ: NotRequired[float]
    refDistance: NotRequired[float]
    maxDistance: NotRequired[float]
    rolloffFactor: NotRequired[float]
    coneInnerAngle: NotRequired[float]
    coneOuterAngle: NotRequired[float]
    coneOuterGain: NotRequired[float]

class PeriodicWave:
    @classmethod
    def new(self, context: BaseAudioContext, options: PeriodicWaveOptions | None = {}) -> PeriodicWave: ...

class PeriodicWaveConstraints(TypedDict):
    disableNormalization: NotRequired[bool]

class PeriodicWaveOptions(TypedDict, PeriodicWaveConstraints):
    real: NotRequired[Sequence[float]]
    imag: NotRequired[Sequence[float]]

class ScriptProcessorNode(AudioNode):
    onaudioprocess: EventHandler
    bufferSize: int

class StereoPannerNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: StereoPannerOptions | None = {}) -> StereoPannerNode: ...
    pan: AudioParam

class StereoPannerOptions(TypedDict, AudioNodeOptions):
    pan: NotRequired[float]

class WaveShaperNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, options: WaveShaperOptions | None = {}) -> WaveShaperNode: ...
    curve: Float32Array
    oversample: OverSampleType

class WaveShaperOptions(TypedDict, AudioNodeOptions):
    curve: NotRequired[Sequence[float]]
    oversample: NotRequired[OverSampleType]

class AudioWorklet(Worklet):
    port: MessagePort

class AudioWorkletGlobalScope(WorkletGlobalScope):
    def registerProcessor(self, name: str, processorCtor: AudioWorkletProcessorConstructor): ...
    currentFrame: int
    currentTime: float
    sampleRate: float
    port: MessagePort

class AudioParamMap: ...

class AudioWorkletNode(AudioNode):
    @classmethod
    def new(self, context: BaseAudioContext, name: str, options: AudioWorkletNodeOptions | None = {}) -> AudioWorkletNode: ...
    parameters: AudioParamMap
    port: MessagePort
    onprocessorerror: EventHandler

class AudioWorkletNodeOptions(TypedDict, AudioNodeOptions):
    numberOfInputs: NotRequired[int]
    numberOfOutputs: NotRequired[int]
    outputChannelCount: NotRequired[Sequence[int]]
    parameterData: NotRequired[float]
    processorOptions: NotRequired[object]

class AudioWorkletProcessor:
    @classmethod
    def new(self) -> AudioWorkletProcessor: ...
    port: MessagePort

class AudioParamDescriptor(TypedDict):
    name: str
    defaultValue: NotRequired[float]
    minValue: NotRequired[float]
    maxValue: NotRequired[float]
    automationRate: NotRequired[AutomationRate]

class PublicKeyCredential(Credential):
    rawId: ArrayBuffer
    response: AuthenticatorResponse
    authenticatorAttachment: str | None
    def getClientExtensionResults(self) -> AuthenticationExtensionsClientOutputs: ...
    def toJSON(self) -> PublicKeyCredentialJSON: ...

class RegistrationResponseJSON(TypedDict):
    id: NotRequired[Base64URLString]
    rawId: NotRequired[Base64URLString]
    response: NotRequired[AuthenticatorAttestationResponseJSON]
    authenticatorAttachment: NotRequired[str | None]
    clientExtensionResults: NotRequired[AuthenticationExtensionsClientOutputsJSON]
    type: NotRequired[str]

class AuthenticatorAttestationResponseJSON(TypedDict):
    clientDataJSON: NotRequired[Base64URLString]
    attestationObject: NotRequired[Base64URLString]
    transports: NotRequired[Sequence[str]]

class AuthenticationResponseJSON(TypedDict):
    id: NotRequired[Base64URLString]
    rawId: NotRequired[Base64URLString]
    response: NotRequired[AuthenticatorAssertionResponseJSON]
    authenticatorAttachment: NotRequired[str | None]
    clientExtensionResults: NotRequired[AuthenticationExtensionsClientOutputsJSON]
    type: NotRequired[str]

class AuthenticatorAssertionResponseJSON(TypedDict):
    clientDataJSON: NotRequired[Base64URLString]
    authenticatorData: NotRequired[Base64URLString]
    signature: NotRequired[Base64URLString]
    userHandle: NotRequired[Base64URLString | None]

class AuthenticationExtensionsClientOutputsJSON(TypedDict): ...

class PublicKeyCredentialCreationOptionsJSON(TypedDict):
    rp: PublicKeyCredentialRpEntity
    user: PublicKeyCredentialUserEntityJSON
    challenge: Base64URLString
    pubKeyCredParams: Sequence[PublicKeyCredentialParameters]
    timeout: NotRequired[int]
    excludeCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptorJSON]]
    authenticatorSelection: NotRequired[AuthenticatorSelectionCriteria]
    attestation: NotRequired[str]
    extensions: NotRequired[AuthenticationExtensionsClientInputsJSON]

class PublicKeyCredentialUserEntityJSON(TypedDict):
    id: Base64URLString
    name: str
    displayName: str

class PublicKeyCredentialDescriptorJSON(TypedDict):
    id: Base64URLString
    type: str
    transports: NotRequired[Sequence[str]]

class AuthenticationExtensionsClientInputsJSON(TypedDict): ...

class PublicKeyCredentialRequestOptionsJSON(TypedDict):
    challenge: Base64URLString
    timeout: NotRequired[int]
    rpId: NotRequired[str]
    allowCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptorJSON]]
    userVerification: NotRequired[str]
    extensions: NotRequired[AuthenticationExtensionsClientInputsJSON]

class AuthenticatorResponse:
    clientDataJSON: ArrayBuffer

class AuthenticatorAttestationResponse(AuthenticatorResponse):
    attestationObject: ArrayBuffer
    def getTransports(self) -> Sequence[str]: ...
    def getAuthenticatorData(self) -> ArrayBuffer: ...
    def getPublicKey(self) -> ArrayBuffer: ...
    def getPublicKeyAlgorithm(self) -> COSEAlgorithmIdentifier: ...

class AuthenticatorAssertionResponse(AuthenticatorResponse):
    authenticatorData: ArrayBuffer
    signature: ArrayBuffer
    userHandle: ArrayBuffer
    attestationObject: ArrayBuffer

class PublicKeyCredentialParameters(TypedDict):
    type: str
    alg: COSEAlgorithmIdentifier

class PublicKeyCredentialCreationOptions(TypedDict):
    rp: PublicKeyCredentialRpEntity
    user: PublicKeyCredentialUserEntity
    challenge: BufferSource
    pubKeyCredParams: Sequence[PublicKeyCredentialParameters]
    timeout: NotRequired[int]
    excludeCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptor]]
    authenticatorSelection: NotRequired[AuthenticatorSelectionCriteria]
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]
    extensions: NotRequired[AuthenticationExtensionsClientInputs]

class PublicKeyCredentialEntity(TypedDict):
    name: str

class PublicKeyCredentialRpEntity(TypedDict, PublicKeyCredentialEntity):
    id: NotRequired[str]

class PublicKeyCredentialUserEntity(TypedDict, PublicKeyCredentialEntity):
    id: BufferSource
    displayName: str

class AuthenticatorSelectionCriteria(TypedDict):
    authenticatorAttachment: NotRequired[str]
    residentKey: NotRequired[str]
    requireResidentKey: NotRequired[bool]
    userVerification: NotRequired[str]

class PublicKeyCredentialRequestOptions(TypedDict):
    challenge: BufferSource
    timeout: NotRequired[int]
    rpId: NotRequired[USVString]
    allowCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptor]]
    userVerification: NotRequired[str]
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]
    extensions: NotRequired[AuthenticationExtensionsClientInputs]

class CollectedClientData(TypedDict):
    type: str
    challenge: str
    origin: str
    crossOrigin: NotRequired[bool]

class TokenBinding(TypedDict):
    status: str
    id: NotRequired[str]

class PublicKeyCredentialDescriptor(TypedDict):
    type: str
    id: BufferSource
    transports: NotRequired[Sequence[str]]

class CredentialPropertiesOutput(TypedDict):
    rk: NotRequired[bool]

class AuthenticationExtensionsPRFValues(TypedDict):
    first: ArrayBuffer
    second: NotRequired[ArrayBuffer]

class AuthenticationExtensionsPRFInputs(TypedDict):
    eval: NotRequired[AuthenticationExtensionsPRFValues]
    evalByCredential: NotRequired[AuthenticationExtensionsPRFValues]

class AuthenticationExtensionsPRFOutputs(TypedDict):
    enabled: NotRequired[bool]
    results: NotRequired[AuthenticationExtensionsPRFValues]

class AuthenticationExtensionsLargeBlobInputs(TypedDict):
    support: NotRequired[str]
    read: NotRequired[bool]
    write: NotRequired[BufferSource]

class AuthenticationExtensionsLargeBlobOutputs(TypedDict):
    supported: NotRequired[bool]
    blob: NotRequired[ArrayBuffer]
    written: NotRequired[bool]

class AuthenticationExtensionsDevicePublicKeyInputs(TypedDict):
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]

class AuthenticationExtensionsDevicePublicKeyOutputs(TypedDict):
    authenticatorOutput: NotRequired[ArrayBuffer]
    signature: NotRequired[ArrayBuffer]

class AudioEncoderConfig(TypedDict, TypedDict, TypedDict, TypedDict):
    aac: NotRequired[AacEncoderConfig]
    flac: NotRequired[FlacEncoderConfig]
    opus: NotRequired[OpusEncoderConfig]
    codec: str
    sampleRate: NotRequired[int]
    numberOfChannels: NotRequired[int]
    bitrate: NotRequired[int]

class AacEncoderConfig(TypedDict):
    format: NotRequired[AacBitstreamFormat]

class VideoEncoderConfig(TypedDict, TypedDict, TypedDict):
    avc: NotRequired[AvcEncoderConfig]
    hevc: NotRequired[HevcEncoderConfig]
    codec: str
    width: int
    height: int
    displayWidth: NotRequired[int]
    displayHeight: NotRequired[int]
    bitrate: NotRequired[int]
    framerate: NotRequired[float]
    hardwareAcceleration: NotRequired[HardwareAcceleration]
    alpha: NotRequired[AlphaOption]
    scalabilityMode: NotRequired[str]
    bitrateMode: NotRequired[BitrateMode]
    latencyMode: NotRequired[LatencyMode]

class AvcEncoderConfig(TypedDict):
    format: NotRequired[AvcBitstreamFormat]

class FlacEncoderConfig(TypedDict):
    blockSize: NotRequired[int]
    compressLevel: NotRequired[int]

class HevcEncoderConfig(TypedDict):
    format: NotRequired[HevcBitstreamFormat]

class OpusEncoderConfig(TypedDict):
    format: NotRequired[OpusBitstreamFormat]
    frameDuration: NotRequired[int]
    complexity: NotRequired[int]
    packetlossperc: NotRequired[int]
    useinbandfec: NotRequired[bool]
    usedtx: NotRequired[bool]

class AudioDecoder:
    @classmethod
    def new(self, init: AudioDecoderInit) -> AudioDecoder: ...
    state: CodecState
    decodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: AudioDecoderConfig): ...
    def decode(self, chunk: EncodedAudioChunk): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class AudioDecoderInit(TypedDict):
    output: AudioDataOutputCallback
    error: WebCodecsErrorCallback

class VideoDecoder:
    @classmethod
    def new(self, init: VideoDecoderInit) -> VideoDecoder: ...
    state: CodecState
    decodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: VideoDecoderConfig): ...
    def decode(self, chunk: EncodedVideoChunk): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class VideoDecoderInit(TypedDict):
    output: VideoFrameOutputCallback
    error: WebCodecsErrorCallback

class AudioEncoder:
    @classmethod
    def new(self, init: AudioEncoderInit) -> AudioEncoder: ...
    state: CodecState
    encodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: AudioEncoderConfig): ...
    def encode(self, data: AudioData): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class AudioEncoderInit(TypedDict):
    output: EncodedAudioChunkOutputCallback
    error: WebCodecsErrorCallback

class EncodedAudioChunkMetadata(TypedDict):
    decoderConfig: NotRequired[AudioDecoderConfig]

class VideoEncoder:
    @classmethod
    def new(self, init: VideoEncoderInit) -> VideoEncoder: ...
    state: CodecState
    encodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: VideoEncoderConfig): ...
    def encode(self, frame: VideoFrame, options: VideoEncoderEncodeOptions | None = {}): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class VideoEncoderInit(TypedDict):
    output: EncodedVideoChunkOutputCallback
    error: WebCodecsErrorCallback

class EncodedVideoChunkMetadata(TypedDict):
    decoderConfig: NotRequired[VideoDecoderConfig]
    svc: NotRequired[SvcOutputMetadata]
    alphaSideData: NotRequired[BufferSource]

class SvcOutputMetadata(TypedDict):
    temporalLayerId: NotRequired[int]

class AudioDecoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[AudioDecoderConfig]

class VideoDecoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[VideoDecoderConfig]

class AudioEncoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[AudioEncoderConfig]

class VideoEncoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[VideoEncoderConfig]

class AudioDecoderConfig(TypedDict):
    codec: str
    sampleRate: int
    numberOfChannels: int
    description: NotRequired[BufferSource]

class VideoDecoderConfig(TypedDict):
    codec: str
    description: NotRequired[BufferSource]
    codedWidth: NotRequired[int]
    codedHeight: NotRequired[int]
    displayAspectWidth: NotRequired[int]
    displayAspectHeight: NotRequired[int]
    colorSpace: NotRequired[VideoColorSpaceInit]
    hardwareAcceleration: NotRequired[HardwareAcceleration]
    optimizeForLatency: NotRequired[bool]

class VideoEncoderEncodeOptions(TypedDict):
    keyFrame: NotRequired[bool]

class EncodedAudioChunk:
    @classmethod
    def new(self, init: EncodedAudioChunkInit) -> EncodedAudioChunk: ...
    type: EncodedAudioChunkType
    timestamp: int
    duration: int | None
    byteLength: int
    def copyTo(self, destination: BufferSource): ...

class EncodedAudioChunkInit(TypedDict):
    type: EncodedAudioChunkType
    timestamp: int
    duration: NotRequired[int]
    data: BufferSource

class EncodedVideoChunk:
    @classmethod
    def new(self, init: EncodedVideoChunkInit) -> EncodedVideoChunk: ...
    type: EncodedVideoChunkType
    timestamp: int
    duration: int | None
    byteLength: int
    def copyTo(self, destination: BufferSource): ...

class EncodedVideoChunkInit(TypedDict):
    type: EncodedVideoChunkType
    timestamp: int
    duration: NotRequired[int]
    data: BufferSource

class AudioData:
    @classmethod
    def new(self, init: AudioDataInit) -> AudioData: ...
    format: AudioSampleFormat | None
    sampleRate: float
    numberOfFrames: int
    numberOfChannels: int
    duration: int
    timestamp: int
    def allocationSize(self, options: AudioDataCopyToOptions) -> int: ...
    def copyTo(self, destination: BufferSource, options: AudioDataCopyToOptions): ...
    def clone(self) -> AudioData: ...
    def close(self): ...

class AudioDataInit(TypedDict):
    format: AudioSampleFormat
    sampleRate: float
    numberOfFrames: int
    numberOfChannels: int
    timestamp: int
    data: BufferSource

class AudioDataCopyToOptions(TypedDict):
    planeIndex: int
    frameOffset: NotRequired[int]
    frameCount: NotRequired[int]
    format: NotRequired[AudioSampleFormat]

class VideoFrame:
    @overload
    @classmethod
    def new(self, image: CanvasImageSource, init: VideoFrameInit | None = {}) -> VideoFrame: ...
    @overload
    @classmethod
    def new(self, data: BufferSource, init: VideoFrameBufferInit) -> VideoFrame: ...
    format: VideoPixelFormat | None
    codedWidth: int
    codedHeight: int
    codedRect: DOMRectReadOnly | None
    visibleRect: DOMRectReadOnly | None
    displayWidth: int
    displayHeight: int
    duration: int | None
    timestamp: int
    colorSpace: VideoColorSpace
    def metadata(self) -> VideoFrameMetadata: ...
    def allocationSize(self, options: VideoFrameCopyToOptions | None = {}) -> int: ...
    def copyTo(self, destination: BufferSource, options: VideoFrameCopyToOptions | None = {}) -> Awaitable[Sequence[PlaneLayout]]: ...
    def clone(self) -> VideoFrame: ...
    def close(self): ...

class VideoFrameInit(TypedDict):
    duration: NotRequired[int]
    timestamp: NotRequired[int]
    alpha: NotRequired[AlphaOption]
    visibleRect: NotRequired[DOMRectInit]
    displayWidth: NotRequired[int]
    displayHeight: NotRequired[int]
    metadata: NotRequired[VideoFrameMetadata]

class VideoFrameBufferInit(TypedDict):
    format: VideoPixelFormat
    codedWidth: int
    codedHeight: int
    timestamp: int
    duration: NotRequired[int]
    layout: NotRequired[Sequence[PlaneLayout]]
    visibleRect: NotRequired[DOMRectInit]
    displayWidth: NotRequired[int]
    displayHeight: NotRequired[int]
    colorSpace: NotRequired[VideoColorSpaceInit]

class VideoFrameMetadata(TypedDict): ...

class VideoFrameCopyToOptions(TypedDict):
    rect: NotRequired[DOMRectInit]
    layout: NotRequired[Sequence[PlaneLayout]]

class PlaneLayout(TypedDict):
    offset: int
    stride: int

class VideoColorSpace:
    @classmethod
    def new(self, init: VideoColorSpaceInit | None = {}) -> VideoColorSpace: ...
    primaries: VideoColorPrimaries | None
    transfer: VideoTransferCharacteristics | None
    matrix: VideoMatrixCoefficients | None
    fullRange: bool | None
    def toJSON(self) -> VideoColorSpaceInit: ...

class VideoColorSpaceInit(TypedDict):
    primaries: NotRequired[VideoColorPrimaries | None]
    transfer: NotRequired[VideoTransferCharacteristics | None]
    matrix: NotRequired[VideoMatrixCoefficients | None]
    fullRange: NotRequired[bool | None]

class ImageDecoder:
    @classmethod
    def new(self, init: ImageDecoderInit) -> ImageDecoder: ...
    type: str
    complete: bool
    completed: Awaitable[None]
    tracks: ImageTrackList
    def decode(self, options: ImageDecodeOptions | None = {}) -> Awaitable[ImageDecodeResult]: ...
    def reset(self): ...
    def close(self): ...

class ImageDecoderInit(TypedDict):
    type: str
    data: ImageBufferSource
    colorSpaceConversion: NotRequired[ColorSpaceConversion]
    desiredWidth: NotRequired[int]
    desiredHeight: NotRequired[int]
    preferAnimation: NotRequired[bool]

class ImageDecodeOptions(TypedDict):
    frameIndex: NotRequired[int]
    completeFramesOnly: NotRequired[bool]

class ImageDecodeResult(TypedDict):
    image: VideoFrame
    complete: bool

class ImageTrackList:
    ready: Awaitable[None]
    length: int
    selectedIndex: int
    selectedTrack: ImageTrack | None

class ImageTrack:
    animated: bool
    frameCount: int
    repetitionCount: float
    selected: bool

class Ed448Params(TypedDict, Algorithm):
    context: NotRequired[BufferSource]

class NavigatorAutomationInformation:
    webdriver: bool

class WebGLContextAttributes(TypedDict, TypedDict):
    alpha: NotRequired[bool]
    depth: NotRequired[bool]
    stencil: NotRequired[bool]
    antialias: NotRequired[bool]
    premultipliedAlpha: NotRequired[bool]
    preserveDrawingBuffer: NotRequired[bool]
    powerPreference: NotRequired[WebGLPowerPreference]
    failIfMajorPerformanceCaveat: NotRequired[bool]
    desynchronized: NotRequired[bool]
    xrCompatible: NotRequired[bool]

class WebGLObject: ...

class WebGLBuffer(WebGLObject): ...

class WebGLFramebuffer(WebGLObject): ...

class WebGLProgram(WebGLObject): ...

class WebGLRenderbuffer(WebGLObject): ...

class WebGLShader(WebGLObject): ...

class WebGLTexture(WebGLObject): ...

class WebGLUniformLocation: ...

class WebGLActiveInfo:
    size: GLint
    type: GLenum
    name: str

class WebGLShaderPrecisionFormat:
    rangeMin: GLint
    rangeMax: GLint
    precision: GLint

class WebGLRenderingContextBase:
    DEPTH_BUFFER_BIT = 0x00000100
    STENCIL_BUFFER_BIT = 0x00000400
    COLOR_BUFFER_BIT = 0x00004000
    POINTS = 0x0000
    LINES = 0x0001
    LINE_LOOP = 0x0002
    LINE_STRIP = 0x0003
    TRIANGLES = 0x0004
    TRIANGLE_STRIP = 0x0005
    TRIANGLE_FAN = 0x0006
    ZERO = 0
    ONE = 1
    SRC_COLOR = 0x0300
    ONE_MINUS_SRC_COLOR = 0x0301
    SRC_ALPHA = 0x0302
    ONE_MINUS_SRC_ALPHA = 0x0303
    DST_ALPHA = 0x0304
    ONE_MINUS_DST_ALPHA = 0x0305
    DST_COLOR = 0x0306
    ONE_MINUS_DST_COLOR = 0x0307
    SRC_ALPHA_SATURATE = 0x0308
    FUNC_ADD = 0x8006
    BLEND_EQUATION = 0x8009
    BLEND_EQUATION_RGB = 0x8009
    BLEND_EQUATION_ALPHA = 0x883D
    FUNC_SUBTRACT = 0x800A
    FUNC_REVERSE_SUBTRACT = 0x800B
    BLEND_DST_RGB = 0x80C8
    BLEND_SRC_RGB = 0x80C9
    BLEND_DST_ALPHA = 0x80CA
    BLEND_SRC_ALPHA = 0x80CB
    CONSTANT_COLOR = 0x8001
    ONE_MINUS_CONSTANT_COLOR = 0x8002
    CONSTANT_ALPHA = 0x8003
    ONE_MINUS_CONSTANT_ALPHA = 0x8004
    BLEND_COLOR = 0x8005
    ARRAY_BUFFER = 0x8892
    ELEMENT_ARRAY_BUFFER = 0x8893
    ARRAY_BUFFER_BINDING = 0x8894
    ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
    STREAM_DRAW = 0x88E0
    STATIC_DRAW = 0x88E4
    DYNAMIC_DRAW = 0x88E8
    BUFFER_SIZE = 0x8764
    BUFFER_USAGE = 0x8765
    CURRENT_VERTEX_ATTRIB = 0x8626
    FRONT = 0x0404
    BACK = 0x0405
    FRONT_AND_BACK = 0x0408
    CULL_FACE = 0x0B44
    BLEND = 0x0BE2
    DITHER = 0x0BD0
    STENCIL_TEST = 0x0B90
    DEPTH_TEST = 0x0B71
    SCISSOR_TEST = 0x0C11
    POLYGON_OFFSET_FILL = 0x8037
    SAMPLE_ALPHA_TO_COVERAGE = 0x809E
    SAMPLE_COVERAGE = 0x80A0
    NO_ERROR = 0
    INVALID_ENUM = 0x0500
    INVALID_VALUE = 0x0501
    INVALID_OPERATION = 0x0502
    OUT_OF_MEMORY = 0x0505
    CW = 0x0900
    CCW = 0x0901
    LINE_WIDTH = 0x0B21
    ALIASED_POINT_SIZE_RANGE = 0x846D
    ALIASED_LINE_WIDTH_RANGE = 0x846E
    CULL_FACE_MODE = 0x0B45
    FRONT_FACE = 0x0B46
    DEPTH_RANGE = 0x0B70
    DEPTH_WRITEMASK = 0x0B72
    DEPTH_CLEAR_VALUE = 0x0B73
    DEPTH_FUNC = 0x0B74
    STENCIL_CLEAR_VALUE = 0x0B91
    STENCIL_FUNC = 0x0B92
    STENCIL_FAIL = 0x0B94
    STENCIL_PASS_DEPTH_FAIL = 0x0B95
    STENCIL_PASS_DEPTH_PASS = 0x0B96
    STENCIL_REF = 0x0B97
    STENCIL_VALUE_MASK = 0x0B93
    STENCIL_WRITEMASK = 0x0B98
    STENCIL_BACK_FUNC = 0x8800
    STENCIL_BACK_FAIL = 0x8801
    STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
    STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
    STENCIL_BACK_REF = 0x8CA3
    STENCIL_BACK_VALUE_MASK = 0x8CA4
    STENCIL_BACK_WRITEMASK = 0x8CA5
    VIEWPORT = 0x0BA2
    SCISSOR_BOX = 0x0C10
    COLOR_CLEAR_VALUE = 0x0C22
    COLOR_WRITEMASK = 0x0C23
    UNPACK_ALIGNMENT = 0x0CF5
    PACK_ALIGNMENT = 0x0D05
    MAX_TEXTURE_SIZE = 0x0D33
    MAX_VIEWPORT_DIMS = 0x0D3A
    SUBPIXEL_BITS = 0x0D50
    RED_BITS = 0x0D52
    GREEN_BITS = 0x0D53
    BLUE_BITS = 0x0D54
    ALPHA_BITS = 0x0D55
    DEPTH_BITS = 0x0D56
    STENCIL_BITS = 0x0D57
    POLYGON_OFFSET_UNITS = 0x2A00
    POLYGON_OFFSET_FACTOR = 0x8038
    TEXTURE_BINDING_2D = 0x8069
    SAMPLE_BUFFERS = 0x80A8
    SAMPLES = 0x80A9
    SAMPLE_COVERAGE_VALUE = 0x80AA
    SAMPLE_COVERAGE_INVERT = 0x80AB
    COMPRESSED_TEXTURE_FORMATS = 0x86A3
    DONT_CARE = 0x1100
    FASTEST = 0x1101
    NICEST = 0x1102
    GENERATE_MIPMAP_HINT = 0x8192
    BYTE = 0x1400
    UNSIGNED_BYTE = 0x1401
    SHORT = 0x1402
    UNSIGNED_SHORT = 0x1403
    INT = 0x1404
    UNSIGNED_INT = 0x1405
    FLOAT = 0x1406
    DEPTH_COMPONENT = 0x1902
    ALPHA = 0x1906
    RGB = 0x1907
    RGBA = 0x1908
    LUMINANCE = 0x1909
    LUMINANCE_ALPHA = 0x190A
    UNSIGNED_SHORT_4_4_4_4 = 0x8033
    UNSIGNED_SHORT_5_5_5_1 = 0x8034
    UNSIGNED_SHORT_5_6_5 = 0x8363
    FRAGMENT_SHADER = 0x8B30
    VERTEX_SHADER = 0x8B31
    MAX_VERTEX_ATTRIBS = 0x8869
    MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
    MAX_VARYING_VECTORS = 0x8DFC
    MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
    MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
    MAX_TEXTURE_IMAGE_UNITS = 0x8872
    MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
    SHADER_TYPE = 0x8B4F
    DELETE_STATUS = 0x8B80
    LINK_STATUS = 0x8B82
    VALIDATE_STATUS = 0x8B83
    ATTACHED_SHADERS = 0x8B85
    ACTIVE_UNIFORMS = 0x8B86
    ACTIVE_ATTRIBUTES = 0x8B89
    SHADING_LANGUAGE_VERSION = 0x8B8C
    CURRENT_PROGRAM = 0x8B8D
    NEVER = 0x0200
    LESS = 0x0201
    EQUAL = 0x0202
    LEQUAL = 0x0203
    GREATER = 0x0204
    NOTEQUAL = 0x0205
    GEQUAL = 0x0206
    ALWAYS = 0x0207
    KEEP = 0x1E00
    REPLACE = 0x1E01
    INCR = 0x1E02
    DECR = 0x1E03
    INVERT = 0x150A
    INCR_WRAP = 0x8507
    DECR_WRAP = 0x8508
    VENDOR = 0x1F00
    RENDERER = 0x1F01
    VERSION = 0x1F02
    NEAREST = 0x2600
    LINEAR = 0x2601
    NEAREST_MIPMAP_NEAREST = 0x2700
    LINEAR_MIPMAP_NEAREST = 0x2701
    NEAREST_MIPMAP_LINEAR = 0x2702
    LINEAR_MIPMAP_LINEAR = 0x2703
    TEXTURE_MAG_FILTER = 0x2800
    TEXTURE_MIN_FILTER = 0x2801
    TEXTURE_WRAP_S = 0x2802
    TEXTURE_WRAP_T = 0x2803
    TEXTURE_2D = 0x0DE1
    TEXTURE = 0x1702
    TEXTURE_CUBE_MAP = 0x8513
    TEXTURE_BINDING_CUBE_MAP = 0x8514
    TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
    TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
    TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
    TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
    TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
    TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
    MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
    TEXTURE0 = 0x84C0
    TEXTURE1 = 0x84C1
    TEXTURE2 = 0x84C2
    TEXTURE3 = 0x84C3
    TEXTURE4 = 0x84C4
    TEXTURE5 = 0x84C5
    TEXTURE6 = 0x84C6
    TEXTURE7 = 0x84C7
    TEXTURE8 = 0x84C8
    TEXTURE9 = 0x84C9
    TEXTURE10 = 0x84CA
    TEXTURE11 = 0x84CB
    TEXTURE12 = 0x84CC
    TEXTURE13 = 0x84CD
    TEXTURE14 = 0x84CE
    TEXTURE15 = 0x84CF
    TEXTURE16 = 0x84D0
    TEXTURE17 = 0x84D1
    TEXTURE18 = 0x84D2
    TEXTURE19 = 0x84D3
    TEXTURE20 = 0x84D4
    TEXTURE21 = 0x84D5
    TEXTURE22 = 0x84D6
    TEXTURE23 = 0x84D7
    TEXTURE24 = 0x84D8
    TEXTURE25 = 0x84D9
    TEXTURE26 = 0x84DA
    TEXTURE27 = 0x84DB
    TEXTURE28 = 0x84DC
    TEXTURE29 = 0x84DD
    TEXTURE30 = 0x84DE
    TEXTURE31 = 0x84DF
    ACTIVE_TEXTURE = 0x84E0
    REPEAT = 0x2901
    CLAMP_TO_EDGE = 0x812F
    MIRRORED_REPEAT = 0x8370
    FLOAT_VEC2 = 0x8B50
    FLOAT_VEC3 = 0x8B51
    FLOAT_VEC4 = 0x8B52
    INT_VEC2 = 0x8B53
    INT_VEC3 = 0x8B54
    INT_VEC4 = 0x8B55
    BOOL = 0x8B56
    BOOL_VEC2 = 0x8B57
    BOOL_VEC3 = 0x8B58
    BOOL_VEC4 = 0x8B59
    FLOAT_MAT2 = 0x8B5A
    FLOAT_MAT3 = 0x8B5B
    FLOAT_MAT4 = 0x8B5C
    SAMPLER_2D = 0x8B5E
    SAMPLER_CUBE = 0x8B60
    VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
    VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
    VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
    VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
    VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
    VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
    VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
    IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
    IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
    COMPILE_STATUS = 0x8B81
    LOW_FLOAT = 0x8DF0
    MEDIUM_FLOAT = 0x8DF1
    HIGH_FLOAT = 0x8DF2
    LOW_INT = 0x8DF3
    MEDIUM_INT = 0x8DF4
    HIGH_INT = 0x8DF5
    FRAMEBUFFER = 0x8D40
    RENDERBUFFER = 0x8D41
    RGBA4 = 0x8056
    RGB5_A1 = 0x8057
    RGB565 = 0x8D62
    DEPTH_COMPONENT16 = 0x81A5
    STENCIL_INDEX8 = 0x8D48
    DEPTH_STENCIL = 0x84F9
    RENDERBUFFER_WIDTH = 0x8D42
    RENDERBUFFER_HEIGHT = 0x8D43
    RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
    RENDERBUFFER_RED_SIZE = 0x8D50
    RENDERBUFFER_GREEN_SIZE = 0x8D51
    RENDERBUFFER_BLUE_SIZE = 0x8D52
    RENDERBUFFER_ALPHA_SIZE = 0x8D53
    RENDERBUFFER_DEPTH_SIZE = 0x8D54
    RENDERBUFFER_STENCIL_SIZE = 0x8D55
    FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
    FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
    FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
    FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
    COLOR_ATTACHMENT0 = 0x8CE0
    DEPTH_ATTACHMENT = 0x8D00
    STENCIL_ATTACHMENT = 0x8D20
    DEPTH_STENCIL_ATTACHMENT = 0x821A
    NONE = 0
    FRAMEBUFFER_COMPLETE = 0x8CD5
    FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
    FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
    FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x8CD9
    FRAMEBUFFER_UNSUPPORTED = 0x8CDD
    FRAMEBUFFER_BINDING = 0x8CA6
    RENDERBUFFER_BINDING = 0x8CA7
    MAX_RENDERBUFFER_SIZE = 0x84E8
    INVALID_FRAMEBUFFER_OPERATION = 0x0506
    UNPACK_FLIP_Y_WEBGL = 0x9240
    UNPACK_PREMULTIPLY_ALPHA_WEBGL = 0x9241
    CONTEXT_LOST_WEBGL = 0x9242
    UNPACK_COLORSPACE_CONVERSION_WEBGL = 0x9243
    BROWSER_DEFAULT_WEBGL = 0x9244
    canvas: HTMLCanvasElement | OffscreenCanvas
    drawingBufferWidth: GLsizei
    drawingBufferHeight: GLsizei
    drawingBufferColorSpace: PredefinedColorSpace
    unpackColorSpace: PredefinedColorSpace
    def getContextAttributes(self) -> WebGLContextAttributes | None: ...
    def isContextLost(self) -> bool: ...
    def getSupportedExtensions(self) -> Sequence[str]: ...
    def getExtension(self, name: str) -> object | None: ...
    def activeTexture(self, texture: GLenum): ...
    def attachShader(self, program: WebGLProgram, shader: WebGLShader): ...
    def bindAttribLocation(self, program: WebGLProgram, index: GLuint, name: str): ...
    def bindBuffer(self, target: GLenum, buffer: WebGLBuffer | None): ...
    def bindFramebuffer(self, target: GLenum, framebuffer: WebGLFramebuffer | None): ...
    def bindRenderbuffer(self, target: GLenum, renderbuffer: WebGLRenderbuffer | None): ...
    def bindTexture(self, target: GLenum, texture: WebGLTexture | None): ...
    def blendColor(self, red: GLclampf, green: GLclampf, blue: GLclampf, alpha: GLclampf): ...
    def blendEquation(self, mode: GLenum): ...
    def blendEquationSeparate(self, modeRGB: GLenum, modeAlpha: GLenum): ...
    def blendFunc(self, sfactor: GLenum, dfactor: GLenum): ...
    def blendFuncSeparate(self, srcRGB: GLenum, dstRGB: GLenum, srcAlpha: GLenum, dstAlpha: GLenum): ...
    def checkFramebufferStatus(self, target: GLenum) -> GLenum: ...
    def clear(self, mask: GLbitfield): ...
    def clearColor(self, red: GLclampf, green: GLclampf, blue: GLclampf, alpha: GLclampf): ...
    def clearDepth(self, depth: GLclampf): ...
    def clearStencil(self, s: GLint): ...
    def colorMask(self, red: GLboolean, green: GLboolean, blue: GLboolean, alpha: GLboolean): ...
    def compileShader(self, shader: WebGLShader): ...
    def copyTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, x: GLint, y: GLint, width: GLsizei, height: GLsizei, border: GLint): ...
    def copyTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def createBuffer(self) -> WebGLBuffer | None: ...
    def createFramebuffer(self) -> WebGLFramebuffer | None: ...
    def createProgram(self) -> WebGLProgram | None: ...
    def createRenderbuffer(self) -> WebGLRenderbuffer | None: ...
    def createShader(self, type: GLenum) -> WebGLShader | None: ...
    def createTexture(self) -> WebGLTexture | None: ...
    def cullFace(self, mode: GLenum): ...
    def deleteBuffer(self, buffer: WebGLBuffer | None): ...
    def deleteFramebuffer(self, framebuffer: WebGLFramebuffer | None): ...
    def deleteProgram(self, program: WebGLProgram | None): ...
    def deleteRenderbuffer(self, renderbuffer: WebGLRenderbuffer | None): ...
    def deleteShader(self, shader: WebGLShader | None): ...
    def deleteTexture(self, texture: WebGLTexture | None): ...
    def depthFunc(self, func: GLenum): ...
    def depthMask(self, flag: GLboolean): ...
    def depthRange(self, zNear: GLclampf, zFar: GLclampf): ...
    def detachShader(self, program: WebGLProgram, shader: WebGLShader): ...
    def disable(self, cap: GLenum): ...
    def disableVertexAttribArray(self, index: GLuint): ...
    def drawArrays(self, mode: GLenum, first: GLint, count: GLsizei): ...
    def drawElements(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr): ...
    def enable(self, cap: GLenum): ...
    def enableVertexAttribArray(self, index: GLuint): ...
    def finish(self): ...
    def flush(self): ...
    def framebufferRenderbuffer(self, target: GLenum, attachment: GLenum, renderbuffertarget: GLenum, renderbuffer: WebGLRenderbuffer | None): ...
    def framebufferTexture2D(self, target: GLenum, attachment: GLenum, textarget: GLenum, texture: WebGLTexture | None, level: GLint): ...
    def frontFace(self, mode: GLenum): ...
    def generateMipmap(self, target: GLenum): ...
    def getActiveAttrib(self, program: WebGLProgram, index: GLuint) -> WebGLActiveInfo | None: ...
    def getActiveUniform(self, program: WebGLProgram, index: GLuint) -> WebGLActiveInfo | None: ...
    def getAttachedShaders(self, program: WebGLProgram) -> Sequence[WebGLShader]: ...
    def getAttribLocation(self, program: WebGLProgram, name: str) -> GLint: ...
    def getBufferParameter(self, target: GLenum, pname: GLenum) -> Any: ...
    def getParameter(self, pname: GLenum) -> Any: ...
    def getError(self) -> GLenum: ...
    def getFramebufferAttachmentParameter(self, target: GLenum, attachment: GLenum, pname: GLenum) -> Any: ...
    def getProgramParameter(self, program: WebGLProgram, pname: GLenum) -> Any: ...
    def getProgramInfoLog(self, program: WebGLProgram) -> str | None: ...
    def getRenderbufferParameter(self, target: GLenum, pname: GLenum) -> Any: ...
    def getShaderParameter(self, shader: WebGLShader, pname: GLenum) -> Any: ...
    def getShaderPrecisionFormat(self, shadertype: GLenum, precisiontype: GLenum) -> WebGLShaderPrecisionFormat | None: ...
    def getShaderInfoLog(self, shader: WebGLShader) -> str | None: ...
    def getShaderSource(self, shader: WebGLShader) -> str | None: ...
    def getTexParameter(self, target: GLenum, pname: GLenum) -> Any: ...
    def getUniform(self, program: WebGLProgram, location: WebGLUniformLocation) -> Any: ...
    def getUniformLocation(self, program: WebGLProgram, name: str) -> WebGLUniformLocation | None: ...
    def getVertexAttrib(self, index: GLuint, pname: GLenum) -> Any: ...
    def getVertexAttribOffset(self, index: GLuint, pname: GLenum) -> GLintptr: ...
    def hint(self, target: GLenum, mode: GLenum): ...
    def isBuffer(self, buffer: WebGLBuffer | None) -> GLboolean: ...
    def isEnabled(self, cap: GLenum) -> GLboolean: ...
    def isFramebuffer(self, framebuffer: WebGLFramebuffer | None) -> GLboolean: ...
    def isProgram(self, program: WebGLProgram | None) -> GLboolean: ...
    def isRenderbuffer(self, renderbuffer: WebGLRenderbuffer | None) -> GLboolean: ...
    def isShader(self, shader: WebGLShader | None) -> GLboolean: ...
    def isTexture(self, texture: WebGLTexture | None) -> GLboolean: ...
    def lineWidth(self, width: GLfloat): ...
    def linkProgram(self, program: WebGLProgram): ...
    def pixelStorei(self, pname: GLenum, param: GLint): ...
    def polygonOffset(self, factor: GLfloat, units: GLfloat): ...
    def renderbufferStorage(self, target: GLenum, internalformat: GLenum, width: GLsizei, height: GLsizei): ...
    def sampleCoverage(self, value: GLclampf, invert: GLboolean): ...
    def scissor(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def shaderSource(self, shader: WebGLShader, source: str): ...
    def stencilFunc(self, func: GLenum, ref: GLint, mask: GLuint): ...
    def stencilFuncSeparate(self, face: GLenum, func: GLenum, ref: GLint, mask: GLuint): ...
    def stencilMask(self, mask: GLuint): ...
    def stencilMaskSeparate(self, face: GLenum, mask: GLuint): ...
    def stencilOp(self, fail: GLenum, zfail: GLenum, zpass: GLenum): ...
    def stencilOpSeparate(self, face: GLenum, fail: GLenum, zfail: GLenum, zpass: GLenum): ...
    def texParameterf(self, target: GLenum, pname: GLenum, param: GLfloat): ...
    def texParameteri(self, target: GLenum, pname: GLenum, param: GLint): ...
    def uniform1f(self, location: WebGLUniformLocation | None, x: GLfloat): ...
    def uniform2f(self, location: WebGLUniformLocation | None, x: GLfloat, y: GLfloat): ...
    def uniform3f(self, location: WebGLUniformLocation | None, x: GLfloat, y: GLfloat, z: GLfloat): ...
    def uniform4f(self, location: WebGLUniformLocation | None, x: GLfloat, y: GLfloat, z: GLfloat, w: GLfloat): ...
    def uniform1i(self, location: WebGLUniformLocation | None, x: GLint): ...
    def uniform2i(self, location: WebGLUniformLocation | None, x: GLint, y: GLint): ...
    def uniform3i(self, location: WebGLUniformLocation | None, x: GLint, y: GLint, z: GLint): ...
    def uniform4i(self, location: WebGLUniformLocation | None, x: GLint, y: GLint, z: GLint, w: GLint): ...
    def useProgram(self, program: WebGLProgram | None): ...
    def validateProgram(self, program: WebGLProgram): ...
    def vertexAttrib1f(self, index: GLuint, x: GLfloat): ...
    def vertexAttrib2f(self, index: GLuint, x: GLfloat, y: GLfloat): ...
    def vertexAttrib3f(self, index: GLuint, x: GLfloat, y: GLfloat, z: GLfloat): ...
    def vertexAttrib4f(self, index: GLuint, x: GLfloat, y: GLfloat, z: GLfloat, w: GLfloat): ...
    def vertexAttrib1fv(self, index: GLuint, values: Float32List): ...
    def vertexAttrib2fv(self, index: GLuint, values: Float32List): ...
    def vertexAttrib3fv(self, index: GLuint, values: Float32List): ...
    def vertexAttrib4fv(self, index: GLuint, values: Float32List): ...
    def vertexAttribPointer(self, index: GLuint, size: GLint, type: GLenum, normalized: GLboolean, stride: GLsizei, offset: GLintptr): ...
    def viewport(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def makeXRCompatible(self) -> Awaitable[None]: ...

class WebGLRenderingContextOverloads:
    @overload
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum): ...
    @overload
    def bufferData(self, target: GLenum, data: BufferSource | None, usage: GLenum): ...
    def bufferSubData(self, target: GLenum, offset: GLintptr, data: BufferSource): ...
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, data: ArrayBufferView): ...
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, data: ArrayBufferView): ...
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    def uniform1fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform2fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform3fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform4fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform1iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniform2iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniform3iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniform4iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniformMatrix2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, value: Float32List): ...
    def uniformMatrix3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, value: Float32List): ...
    def uniformMatrix4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, value: Float32List): ...

class WebGLRenderingContext(WebGLRenderingContextBase, WebGLRenderingContextOverloads): ...

class WebGLContextEvent(Event):
    @classmethod
    def new(self, type: str, eventInit: WebGLContextEventInit | None = {}) -> WebGLContextEvent: ...
    statusMessage: str

class WebGLContextEventInit(TypedDict, EventInit):
    statusMessage: NotRequired[str]

class WebGLQuery(WebGLObject): ...

class WebGLSampler(WebGLObject): ...

class WebGLSync(WebGLObject): ...

class WebGLTransformFeedback(WebGLObject): ...

class WebGLVertexArrayObject(WebGLObject): ...

class WebGL2RenderingContextBase:
    READ_BUFFER = 0x0C02
    UNPACK_ROW_LENGTH = 0x0CF2
    UNPACK_SKIP_ROWS = 0x0CF3
    UNPACK_SKIP_PIXELS = 0x0CF4
    PACK_ROW_LENGTH = 0x0D02
    PACK_SKIP_ROWS = 0x0D03
    PACK_SKIP_PIXELS = 0x0D04
    COLOR = 0x1800
    DEPTH = 0x1801
    STENCIL = 0x1802
    RED = 0x1903
    RGB8 = 0x8051
    RGBA8 = 0x8058
    RGB10_A2 = 0x8059
    TEXTURE_BINDING_3D = 0x806A
    UNPACK_SKIP_IMAGES = 0x806D
    UNPACK_IMAGE_HEIGHT = 0x806E
    TEXTURE_3D = 0x806F
    TEXTURE_WRAP_R = 0x8072
    MAX_3D_TEXTURE_SIZE = 0x8073
    UNSIGNED_INT_2_10_10_10_REV = 0x8368
    MAX_ELEMENTS_VERTICES = 0x80E8
    MAX_ELEMENTS_INDICES = 0x80E9
    TEXTURE_MIN_LOD = 0x813A
    TEXTURE_MAX_LOD = 0x813B
    TEXTURE_BASE_LEVEL = 0x813C
    TEXTURE_MAX_LEVEL = 0x813D
    MIN = 0x8007
    MAX = 0x8008
    DEPTH_COMPONENT24 = 0x81A6
    MAX_TEXTURE_LOD_BIAS = 0x84FD
    TEXTURE_COMPARE_MODE = 0x884C
    TEXTURE_COMPARE_FUNC = 0x884D
    CURRENT_QUERY = 0x8865
    QUERY_RESULT = 0x8866
    QUERY_RESULT_AVAILABLE = 0x8867
    STREAM_READ = 0x88E1
    STREAM_COPY = 0x88E2
    STATIC_READ = 0x88E5
    STATIC_COPY = 0x88E6
    DYNAMIC_READ = 0x88E9
    DYNAMIC_COPY = 0x88EA
    MAX_DRAW_BUFFERS = 0x8824
    DRAW_BUFFER0 = 0x8825
    DRAW_BUFFER1 = 0x8826
    DRAW_BUFFER2 = 0x8827
    DRAW_BUFFER3 = 0x8828
    DRAW_BUFFER4 = 0x8829
    DRAW_BUFFER5 = 0x882A
    DRAW_BUFFER6 = 0x882B
    DRAW_BUFFER7 = 0x882C
    DRAW_BUFFER8 = 0x882D
    DRAW_BUFFER9 = 0x882E
    DRAW_BUFFER10 = 0x882F
    DRAW_BUFFER11 = 0x8830
    DRAW_BUFFER12 = 0x8831
    DRAW_BUFFER13 = 0x8832
    DRAW_BUFFER14 = 0x8833
    DRAW_BUFFER15 = 0x8834
    MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
    MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
    SAMPLER_3D = 0x8B5F
    SAMPLER_2D_SHADOW = 0x8B62
    FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
    PIXEL_PACK_BUFFER = 0x88EB
    PIXEL_UNPACK_BUFFER = 0x88EC
    PIXEL_PACK_BUFFER_BINDING = 0x88ED
    PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
    FLOAT_MAT2x3 = 0x8B65
    FLOAT_MAT2x4 = 0x8B66
    FLOAT_MAT3x2 = 0x8B67
    FLOAT_MAT3x4 = 0x8B68
    FLOAT_MAT4x2 = 0x8B69
    FLOAT_MAT4x3 = 0x8B6A
    SRGB = 0x8C40
    SRGB8 = 0x8C41
    SRGB8_ALPHA8 = 0x8C43
    COMPARE_REF_TO_TEXTURE = 0x884E
    RGBA32F = 0x8814
    RGB32F = 0x8815
    RGBA16F = 0x881A
    RGB16F = 0x881B
    VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
    MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
    MIN_PROGRAM_TEXEL_OFFSET = 0x8904
    MAX_PROGRAM_TEXEL_OFFSET = 0x8905
    MAX_VARYING_COMPONENTS = 0x8B4B
    TEXTURE_2D_ARRAY = 0x8C1A
    TEXTURE_BINDING_2D_ARRAY = 0x8C1D
    R11F_G11F_B10F = 0x8C3A
    UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
    RGB9_E5 = 0x8C3D
    UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
    TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
    MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
    TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
    TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
    TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
    TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
    RASTERIZER_DISCARD = 0x8C89
    MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
    MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
    INTERLEAVED_ATTRIBS = 0x8C8C
    SEPARATE_ATTRIBS = 0x8C8D
    TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
    TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
    RGBA32UI = 0x8D70
    RGB32UI = 0x8D71
    RGBA16UI = 0x8D76
    RGB16UI = 0x8D77
    RGBA8UI = 0x8D7C
    RGB8UI = 0x8D7D
    RGBA32I = 0x8D82
    RGB32I = 0x8D83
    RGBA16I = 0x8D88
    RGB16I = 0x8D89
    RGBA8I = 0x8D8E
    RGB8I = 0x8D8F
    RED_INTEGER = 0x8D94
    RGB_INTEGER = 0x8D98
    RGBA_INTEGER = 0x8D99
    SAMPLER_2D_ARRAY = 0x8DC1
    SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
    SAMPLER_CUBE_SHADOW = 0x8DC5
    UNSIGNED_INT_VEC2 = 0x8DC6
    UNSIGNED_INT_VEC3 = 0x8DC7
    UNSIGNED_INT_VEC4 = 0x8DC8
    INT_SAMPLER_2D = 0x8DCA
    INT_SAMPLER_3D = 0x8DCB
    INT_SAMPLER_CUBE = 0x8DCC
    INT_SAMPLER_2D_ARRAY = 0x8DCF
    UNSIGNED_INT_SAMPLER_2D = 0x8DD2
    UNSIGNED_INT_SAMPLER_3D = 0x8DD3
    UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
    UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
    DEPTH_COMPONENT32F = 0x8CAC
    DEPTH32F_STENCIL8 = 0x8CAD
    FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
    FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
    FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
    FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
    FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
    FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
    FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
    FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
    FRAMEBUFFER_DEFAULT = 0x8218
    UNSIGNED_INT_24_8 = 0x84FA
    DEPTH24_STENCIL8 = 0x88F0
    UNSIGNED_NORMALIZED = 0x8C17
    DRAW_FRAMEBUFFER_BINDING = 0x8CA6
    READ_FRAMEBUFFER = 0x8CA8
    DRAW_FRAMEBUFFER = 0x8CA9
    READ_FRAMEBUFFER_BINDING = 0x8CAA
    RENDERBUFFER_SAMPLES = 0x8CAB
    FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
    MAX_COLOR_ATTACHMENTS = 0x8CDF
    COLOR_ATTACHMENT1 = 0x8CE1
    COLOR_ATTACHMENT2 = 0x8CE2
    COLOR_ATTACHMENT3 = 0x8CE3
    COLOR_ATTACHMENT4 = 0x8CE4
    COLOR_ATTACHMENT5 = 0x8CE5
    COLOR_ATTACHMENT6 = 0x8CE6
    COLOR_ATTACHMENT7 = 0x8CE7
    COLOR_ATTACHMENT8 = 0x8CE8
    COLOR_ATTACHMENT9 = 0x8CE9
    COLOR_ATTACHMENT10 = 0x8CEA
    COLOR_ATTACHMENT11 = 0x8CEB
    COLOR_ATTACHMENT12 = 0x8CEC
    COLOR_ATTACHMENT13 = 0x8CED
    COLOR_ATTACHMENT14 = 0x8CEE
    COLOR_ATTACHMENT15 = 0x8CEF
    FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
    MAX_SAMPLES = 0x8D57
    HALF_FLOAT = 0x140B
    RG = 0x8227
    RG_INTEGER = 0x8228
    R8 = 0x8229
    RG8 = 0x822B
    R16F = 0x822D
    R32F = 0x822E
    RG16F = 0x822F
    RG32F = 0x8230
    R8I = 0x8231
    R8UI = 0x8232
    R16I = 0x8233
    R16UI = 0x8234
    R32I = 0x8235
    R32UI = 0x8236
    RG8I = 0x8237
    RG8UI = 0x8238
    RG16I = 0x8239
    RG16UI = 0x823A
    RG32I = 0x823B
    RG32UI = 0x823C
    VERTEX_ARRAY_BINDING = 0x85B5
    R8_SNORM = 0x8F94
    RG8_SNORM = 0x8F95
    RGB8_SNORM = 0x8F96
    RGBA8_SNORM = 0x8F97
    SIGNED_NORMALIZED = 0x8F9C
    COPY_READ_BUFFER = 0x8F36
    COPY_WRITE_BUFFER = 0x8F37
    COPY_READ_BUFFER_BINDING = 0x8F36
    COPY_WRITE_BUFFER_BINDING = 0x8F37
    UNIFORM_BUFFER = 0x8A11
    UNIFORM_BUFFER_BINDING = 0x8A28
    UNIFORM_BUFFER_START = 0x8A29
    UNIFORM_BUFFER_SIZE = 0x8A2A
    MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
    MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
    MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
    MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
    MAX_UNIFORM_BLOCK_SIZE = 0x8A30
    MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
    MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
    UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
    ACTIVE_UNIFORM_BLOCKS = 0x8A36
    UNIFORM_TYPE = 0x8A37
    UNIFORM_SIZE = 0x8A38
    UNIFORM_BLOCK_INDEX = 0x8A3A
    UNIFORM_OFFSET = 0x8A3B
    UNIFORM_ARRAY_STRIDE = 0x8A3C
    UNIFORM_MATRIX_STRIDE = 0x8A3D
    UNIFORM_IS_ROW_MAJOR = 0x8A3E
    UNIFORM_BLOCK_BINDING = 0x8A3F
    UNIFORM_BLOCK_DATA_SIZE = 0x8A40
    UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
    UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
    UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
    UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
    INVALID_INDEX = 0xFFFFFFFF
    MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
    MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
    MAX_SERVER_WAIT_TIMEOUT = 0x9111
    OBJECT_TYPE = 0x9112
    SYNC_CONDITION = 0x9113
    SYNC_STATUS = 0x9114
    SYNC_FLAGS = 0x9115
    SYNC_FENCE = 0x9116
    SYNC_GPU_COMMANDS_COMPLETE = 0x9117
    UNSIGNALED = 0x9118
    SIGNALED = 0x9119
    ALREADY_SIGNALED = 0x911A
    TIMEOUT_EXPIRED = 0x911B
    CONDITION_SATISFIED = 0x911C
    WAIT_FAILED = 0x911D
    SYNC_FLUSH_COMMANDS_BIT = 0x00000001
    VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
    ANY_SAMPLES_PASSED = 0x8C2F
    ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
    SAMPLER_BINDING = 0x8919
    RGB10_A2UI = 0x906F
    INT_2_10_10_10_REV = 0x8D9F
    TRANSFORM_FEEDBACK = 0x8E22
    TRANSFORM_FEEDBACK_PAUSED = 0x8E23
    TRANSFORM_FEEDBACK_ACTIVE = 0x8E24
    TRANSFORM_FEEDBACK_BINDING = 0x8E25
    TEXTURE_IMMUTABLE_FORMAT = 0x912F
    MAX_ELEMENT_INDEX = 0x8D6B
    TEXTURE_IMMUTABLE_LEVELS = 0x82DF
    TIMEOUT_IGNORED = -1
    MAX_CLIENT_WAIT_TIMEOUT_WEBGL = 0x9247
    def copyBufferSubData(self, readTarget: GLenum, writeTarget: GLenum, readOffset: GLintptr, writeOffset: GLintptr, size: GLsizeiptr): ...
    def getBufferSubData(self, target: GLenum, srcByteOffset: GLintptr, dstBuffer: ArrayBufferView, dstOffset: GLuint | None = 0, length: GLuint | None = 0): ...
    def blitFramebuffer(self, srcX0: GLint, srcY0: GLint, srcX1: GLint, srcY1: GLint, dstX0: GLint, dstY0: GLint, dstX1: GLint, dstY1: GLint, mask: GLbitfield, filter: GLenum): ...
    def framebufferTextureLayer(self, target: GLenum, attachment: GLenum, texture: WebGLTexture | None, level: GLint, layer: GLint): ...
    def invalidateFramebuffer(self, target: GLenum, attachments: Sequence[GLenum]): ...
    def invalidateSubFramebuffer(self, target: GLenum, attachments: Sequence[GLenum], x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def readBuffer(self, src: GLenum): ...
    def getInternalformatParameter(self, target: GLenum, internalformat: GLenum, pname: GLenum) -> Any: ...
    def renderbufferStorageMultisample(self, target: GLenum, samples: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei): ...
    def texStorage2D(self, target: GLenum, levels: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei): ...
    def texStorage3D(self, target: GLenum, levels: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView | None): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint): ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, srcData: ArrayBufferView | None, srcOffset: GLuint | None = 0): ...
    def copyTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    @overload
    def compressedTexImage3D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexImage3D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    @overload
    def compressedTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    def getFragDataLocation(self, program: WebGLProgram, name: str) -> GLint: ...
    def uniform1ui(self, location: WebGLUniformLocation | None, v0: GLuint): ...
    def uniform2ui(self, location: WebGLUniformLocation | None, v0: GLuint, v1: GLuint): ...
    def uniform3ui(self, location: WebGLUniformLocation | None, v0: GLuint, v1: GLuint, v2: GLuint): ...
    def uniform4ui(self, location: WebGLUniformLocation | None, v0: GLuint, v1: GLuint, v2: GLuint, v3: GLuint): ...
    def uniform1uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform2uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform3uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform4uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix3x2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix4x2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix2x3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix4x3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix2x4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix3x4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def vertexAttribI4i(self, index: GLuint, x: GLint, y: GLint, z: GLint, w: GLint): ...
    def vertexAttribI4iv(self, index: GLuint, values: Int32List): ...
    def vertexAttribI4ui(self, index: GLuint, x: GLuint, y: GLuint, z: GLuint, w: GLuint): ...
    def vertexAttribI4uiv(self, index: GLuint, values: Uint32List): ...
    def vertexAttribIPointer(self, index: GLuint, size: GLint, type: GLenum, stride: GLsizei, offset: GLintptr): ...
    def vertexAttribDivisor(self, index: GLuint, divisor: GLuint): ...
    def drawArraysInstanced(self, mode: GLenum, first: GLint, count: GLsizei, instanceCount: GLsizei): ...
    def drawElementsInstanced(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, instanceCount: GLsizei): ...
    def drawRangeElements(self, mode: GLenum, start: GLuint, end: GLuint, count: GLsizei, type: GLenum, offset: GLintptr): ...
    def drawBuffers(self, buffers: Sequence[GLenum]): ...
    def clearBufferfv(self, buffer: GLenum, drawbuffer: GLint, values: Float32List, srcOffset: GLuint | None = 0): ...
    def clearBufferiv(self, buffer: GLenum, drawbuffer: GLint, values: Int32List, srcOffset: GLuint | None = 0): ...
    def clearBufferuiv(self, buffer: GLenum, drawbuffer: GLint, values: Uint32List, srcOffset: GLuint | None = 0): ...
    def clearBufferfi(self, buffer: GLenum, drawbuffer: GLint, depth: GLfloat, stencil: GLint): ...
    def createQuery(self) -> WebGLQuery | None: ...
    def deleteQuery(self, query: WebGLQuery | None): ...
    def isQuery(self, query: WebGLQuery | None) -> GLboolean: ...
    def beginQuery(self, target: GLenum, query: WebGLQuery): ...
    def endQuery(self, target: GLenum): ...
    def getQuery(self, target: GLenum, pname: GLenum) -> WebGLQuery | None: ...
    def getQueryParameter(self, query: WebGLQuery, pname: GLenum) -> Any: ...
    def createSampler(self) -> WebGLSampler | None: ...
    def deleteSampler(self, sampler: WebGLSampler | None): ...
    def isSampler(self, sampler: WebGLSampler | None) -> GLboolean: ...
    def bindSampler(self, unit: GLuint, sampler: WebGLSampler | None): ...
    def samplerParameteri(self, sampler: WebGLSampler, pname: GLenum, param: GLint): ...
    def samplerParameterf(self, sampler: WebGLSampler, pname: GLenum, param: GLfloat): ...
    def getSamplerParameter(self, sampler: WebGLSampler, pname: GLenum) -> Any: ...
    def fenceSync(self, condition: GLenum, flags: GLbitfield) -> WebGLSync | None: ...
    def isSync(self, sync: WebGLSync | None) -> GLboolean: ...
    def deleteSync(self, sync: WebGLSync | None): ...
    def clientWaitSync(self, sync: WebGLSync, flags: GLbitfield, timeout: GLuint64) -> GLenum: ...
    def waitSync(self, sync: WebGLSync, flags: GLbitfield, timeout: GLint64): ...
    def getSyncParameter(self, sync: WebGLSync, pname: GLenum) -> Any: ...
    def createTransformFeedback(self) -> WebGLTransformFeedback | None: ...
    def deleteTransformFeedback(self, tf: WebGLTransformFeedback | None): ...
    def isTransformFeedback(self, tf: WebGLTransformFeedback | None) -> GLboolean: ...
    def bindTransformFeedback(self, target: GLenum, tf: WebGLTransformFeedback | None): ...
    def beginTransformFeedback(self, primitiveMode: GLenum): ...
    def endTransformFeedback(self): ...
    def transformFeedbackVaryings(self, program: WebGLProgram, varyings: Sequence[str], bufferMode: GLenum): ...
    def getTransformFeedbackVarying(self, program: WebGLProgram, index: GLuint) -> WebGLActiveInfo | None: ...
    def pauseTransformFeedback(self): ...
    def resumeTransformFeedback(self): ...
    def bindBufferBase(self, target: GLenum, index: GLuint, buffer: WebGLBuffer | None): ...
    def bindBufferRange(self, target: GLenum, index: GLuint, buffer: WebGLBuffer | None, offset: GLintptr, size: GLsizeiptr): ...
    def getIndexedParameter(self, target: GLenum, index: GLuint) -> Any: ...
    def getUniformIndices(self, program: WebGLProgram, uniformNames: Sequence[str]) -> Sequence[GLuint]: ...
    def getActiveUniforms(self, program: WebGLProgram, uniformIndices: Sequence[GLuint], pname: GLenum) -> Any: ...
    def getUniformBlockIndex(self, program: WebGLProgram, uniformBlockName: str) -> GLuint: ...
    def getActiveUniformBlockParameter(self, program: WebGLProgram, uniformBlockIndex: GLuint, pname: GLenum) -> Any: ...
    def getActiveUniformBlockName(self, program: WebGLProgram, uniformBlockIndex: GLuint) -> str | None: ...
    def uniformBlockBinding(self, program: WebGLProgram, uniformBlockIndex: GLuint, uniformBlockBinding: GLuint): ...
    def createVertexArray(self) -> WebGLVertexArrayObject | None: ...
    def deleteVertexArray(self, vertexArray: WebGLVertexArrayObject | None): ...
    def isVertexArray(self, vertexArray: WebGLVertexArrayObject | None) -> GLboolean: ...
    def bindVertexArray(self, array: WebGLVertexArrayObject | None): ...

class WebGL2RenderingContextOverloads:
    @overload
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum): ...
    @overload
    def bufferData(self, target: GLenum, srcData: BufferSource | None, usage: GLenum): ...
    @overload
    def bufferSubData(self, target: GLenum, dstByteOffset: GLintptr, srcData: BufferSource): ...
    @overload
    def bufferData(self, target: GLenum, srcData: ArrayBufferView, usage: GLenum, srcOffset: GLuint, length: GLuint | None = 0): ...
    @overload
    def bufferSubData(self, target: GLenum, dstByteOffset: GLintptr, srcData: ArrayBufferView, srcOffset: GLuint, length: GLuint | None = 0): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint): ...
    @overload
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    @overload
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    def uniform1fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform2fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform3fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform4fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform1iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform2iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform3iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform4iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, dstData: ArrayBufferView | None): ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, offset: GLintptr): ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, dstData: ArrayBufferView, dstOffset: GLuint): ...

class WebGL2RenderingContext(WebGLRenderingContextBase, WebGL2RenderingContextBase, WebGL2RenderingContextOverloads): ...

class GPUObjectBase:
    label: USVString

class GPUObjectDescriptorBase(TypedDict):
    label: NotRequired[USVString]

class GPUSupportedLimits:
    maxTextureDimension1D: int
    maxTextureDimension2D: int
    maxTextureDimension3D: int
    maxTextureArrayLayers: int
    maxBindGroups: int
    maxBindingsPerBindGroup: int
    maxDynamicUniformBuffersPerPipelineLayout: int
    maxDynamicStorageBuffersPerPipelineLayout: int
    maxSampledTexturesPerShaderStage: int
    maxSamplersPerShaderStage: int
    maxStorageBuffersPerShaderStage: int
    maxStorageTexturesPerShaderStage: int
    maxUniformBuffersPerShaderStage: int
    maxUniformBufferBindingSize: int
    maxStorageBufferBindingSize: int
    minUniformBufferOffsetAlignment: int
    minStorageBufferOffsetAlignment: int
    maxVertexBuffers: int
    maxBufferSize: int
    maxVertexAttributes: int
    maxVertexBufferArrayStride: int
    maxInterStageShaderComponents: int
    maxInterStageShaderVariables: int
    maxColorAttachments: int
    maxColorAttachmentBytesPerSample: int
    maxComputeWorkgroupStorageSize: int
    maxComputeInvocationsPerWorkgroup: int
    maxComputeWorkgroupSizeX: int
    maxComputeWorkgroupSizeY: int
    maxComputeWorkgroupSizeZ: int
    maxComputeWorkgroupsPerDimension: int

class GPUSupportedFeatures: ...

class GPUAdapterInfo:
    vendor: str
    architecture: str
    device: str
    description: str

class NavigatorGPU:
    gpu: GPU

class GPU:
    def requestAdapter(self, options: GPURequestAdapterOptions | None = {}) -> Awaitable[GPUAdapter | None]: ...
    def getPreferredCanvasFormat(self) -> GPUTextureFormat: ...

class GPURequestAdapterOptions(TypedDict):
    powerPreference: NotRequired[GPUPowerPreference]
    forceFallbackAdapter: NotRequired[bool]

class GPUAdapter:
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    isFallbackAdapter: bool
    def requestDevice(self, descriptor: GPUDeviceDescriptor | None = {}) -> Awaitable[GPUDevice]: ...
    def requestAdapterInfo(self, unmaskHints: Sequence[str] | None = []) -> Awaitable[GPUAdapterInfo]: ...

class GPUDeviceDescriptor(TypedDict, GPUObjectDescriptorBase):
    requiredFeatures: NotRequired[Sequence[GPUFeatureName]]
    requiredLimits: NotRequired[GPUSize64]
    defaultQueue: NotRequired[GPUQueueDescriptor]

class GPUDevice(EventTarget, GPUObjectBase):
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    queue: GPUQueue
    def destroy(self): ...
    def createBuffer(self, descriptor: GPUBufferDescriptor) -> GPUBuffer: ...
    def createTexture(self, descriptor: GPUTextureDescriptor) -> GPUTexture: ...
    def createSampler(self, descriptor: GPUSamplerDescriptor | None = {}) -> GPUSampler: ...
    def importExternalTexture(self, descriptor: GPUExternalTextureDescriptor) -> GPUExternalTexture: ...
    def createBindGroupLayout(self, descriptor: GPUBindGroupLayoutDescriptor) -> GPUBindGroupLayout: ...
    def createPipelineLayout(self, descriptor: GPUPipelineLayoutDescriptor) -> GPUPipelineLayout: ...
    def createBindGroup(self, descriptor: GPUBindGroupDescriptor) -> GPUBindGroup: ...
    def createShaderModule(self, descriptor: GPUShaderModuleDescriptor) -> GPUShaderModule: ...
    def createComputePipeline(self, descriptor: GPUComputePipelineDescriptor) -> GPUComputePipeline: ...
    def createRenderPipeline(self, descriptor: GPURenderPipelineDescriptor) -> GPURenderPipeline: ...
    def createComputePipelineAsync(self, descriptor: GPUComputePipelineDescriptor) -> Awaitable[GPUComputePipeline]: ...
    def createRenderPipelineAsync(self, descriptor: GPURenderPipelineDescriptor) -> Awaitable[GPURenderPipeline]: ...
    def createCommandEncoder(self, descriptor: GPUCommandEncoderDescriptor | None = {}) -> GPUCommandEncoder: ...
    def createRenderBundleEncoder(self, descriptor: GPURenderBundleEncoderDescriptor) -> GPURenderBundleEncoder: ...
    def createQuerySet(self, descriptor: GPUQuerySetDescriptor) -> GPUQuerySet: ...
    lost: Awaitable[GPUDeviceLostInfo]
    def pushErrorScope(self, filter: GPUErrorFilter): ...
    def popErrorScope(self) -> Awaitable[GPUError | None]: ...
    onuncapturederror: EventHandler

class GPUBuffer(GPUObjectBase):
    size: GPUSize64
    usage: GPUBufferUsageFlags
    mapState: GPUBufferMapState
    def mapAsync(self, mode: GPUMapModeFlags, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None) -> Awaitable[None]: ...
    def getMappedRange(self, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None) -> ArrayBuffer: ...
    def unmap(self): ...
    def destroy(self): ...

class GPUBufferDescriptor(TypedDict, GPUObjectDescriptorBase):
    size: GPUSize64
    usage: GPUBufferUsageFlags
    mappedAtCreation: NotRequired[bool]

class GPUTexture(GPUObjectBase):
    def createView(self, descriptor: GPUTextureViewDescriptor | None = {}) -> GPUTextureView: ...
    def destroy(self): ...
    width: GPUIntegerCoordinate
    height: GPUIntegerCoordinate
    depthOrArrayLayers: GPUIntegerCoordinate
    mipLevelCount: GPUIntegerCoordinate
    sampleCount: GPUSize32
    dimension: GPUTextureDimension
    format: GPUTextureFormat
    usage: GPUTextureUsageFlags

class GPUTextureDescriptor(TypedDict, GPUObjectDescriptorBase):
    size: GPUExtent3D
    mipLevelCount: NotRequired[GPUIntegerCoordinate]
    sampleCount: NotRequired[GPUSize32]
    dimension: NotRequired[GPUTextureDimension]
    format: GPUTextureFormat
    usage: GPUTextureUsageFlags
    viewFormats: NotRequired[Sequence[GPUTextureFormat]]

class GPUTextureView(GPUObjectBase): ...

class GPUTextureViewDescriptor(TypedDict, GPUObjectDescriptorBase):
    format: NotRequired[GPUTextureFormat]
    dimension: NotRequired[GPUTextureViewDimension]
    aspect: NotRequired[GPUTextureAspect]
    baseMipLevel: NotRequired[GPUIntegerCoordinate]
    mipLevelCount: NotRequired[GPUIntegerCoordinate]
    baseArrayLayer: NotRequired[GPUIntegerCoordinate]
    arrayLayerCount: NotRequired[GPUIntegerCoordinate]

class GPUExternalTexture(GPUObjectBase):
    expired: bool

class GPUExternalTextureDescriptor(TypedDict, GPUObjectDescriptorBase):
    source: HTMLVideoElement
    colorSpace: NotRequired[PredefinedColorSpace]

class GPUSampler(GPUObjectBase): ...

class GPUSamplerDescriptor(TypedDict, GPUObjectDescriptorBase):
    addressModeU: NotRequired[GPUAddressMode]
    addressModeV: NotRequired[GPUAddressMode]
    addressModeW: NotRequired[GPUAddressMode]
    magFilter: NotRequired[GPUFilterMode]
    minFilter: NotRequired[GPUFilterMode]
    mipmapFilter: NotRequired[GPUMipmapFilterMode]
    lodMinClamp: NotRequired[float]
    lodMaxClamp: NotRequired[float]
    compare: NotRequired[GPUCompareFunction]
    maxAnisotropy: NotRequired[int]

class GPUBindGroupLayout(GPUObjectBase): ...

class GPUBindGroupLayoutDescriptor(TypedDict, GPUObjectDescriptorBase):
    entries: Sequence[GPUBindGroupLayoutEntry]

class GPUBindGroupLayoutEntry(TypedDict):
    binding: GPUIndex32
    visibility: GPUShaderStageFlags
    buffer: NotRequired[GPUBufferBindingLayout]
    sampler: NotRequired[GPUSamplerBindingLayout]
    texture: NotRequired[GPUTextureBindingLayout]
    storageTexture: NotRequired[GPUStorageTextureBindingLayout]
    externalTexture: NotRequired[GPUExternalTextureBindingLayout]

class GPUBufferBindingLayout(TypedDict):
    type: NotRequired[GPUBufferBindingType]
    hasDynamicOffset: NotRequired[bool]
    minBindingSize: NotRequired[GPUSize64]

class GPUSamplerBindingLayout(TypedDict):
    type: NotRequired[GPUSamplerBindingType]

class GPUTextureBindingLayout(TypedDict):
    sampleType: NotRequired[GPUTextureSampleType]
    viewDimension: NotRequired[GPUTextureViewDimension]
    multisampled: NotRequired[bool]

class GPUStorageTextureBindingLayout(TypedDict):
    access: NotRequired[GPUStorageTextureAccess]
    format: GPUTextureFormat
    viewDimension: NotRequired[GPUTextureViewDimension]

class GPUExternalTextureBindingLayout(TypedDict): ...

class GPUBindGroup(GPUObjectBase): ...

class GPUBindGroupDescriptor(TypedDict, GPUObjectDescriptorBase):
    layout: GPUBindGroupLayout
    entries: Sequence[GPUBindGroupEntry]

class GPUBindGroupEntry(TypedDict):
    binding: GPUIndex32
    resource: GPUBindingResource

class GPUBufferBinding(TypedDict):
    buffer: GPUBuffer
    offset: NotRequired[GPUSize64]
    size: NotRequired[GPUSize64]

class GPUPipelineLayout(GPUObjectBase): ...

class GPUPipelineLayoutDescriptor(TypedDict, GPUObjectDescriptorBase):
    bindGroupLayouts: Sequence[GPUBindGroupLayout]

class GPUShaderModule(GPUObjectBase):
    def compilationInfo(self) -> Awaitable[GPUCompilationInfo]: ...

class GPUShaderModuleDescriptor(TypedDict, GPUObjectDescriptorBase):
    code: USVString
    sourceMap: NotRequired[object]
    hints: NotRequired[GPUShaderModuleCompilationHint]

class GPUShaderModuleCompilationHint(TypedDict):
    layout: NotRequired[GPUPipelineLayout | GPUAutoLayoutMode]

class GPUCompilationMessage:
    message: str
    type: GPUCompilationMessageType
    lineNum: int
    linePos: int
    offset: int
    length: int

class GPUCompilationInfo:
    messages: Sequence[GPUCompilationMessage]

class GPUPipelineError(DOMException):
    @classmethod
    def new(self, message: str, options: GPUPipelineErrorInit) -> GPUPipelineError: ...
    reason: GPUPipelineErrorReason

class GPUPipelineErrorInit(TypedDict):
    reason: GPUPipelineErrorReason

class GPUPipelineDescriptorBase(TypedDict, GPUObjectDescriptorBase):
    layout: GPUPipelineLayout | GPUAutoLayoutMode

class GPUPipelineBase:
    def getBindGroupLayout(self, index: int) -> GPUBindGroupLayout: ...

class GPUProgrammableStage(TypedDict):
    module: GPUShaderModule
    entryPoint: USVString
    constants: NotRequired[GPUPipelineConstantValue]

class GPUComputePipeline(GPUObjectBase, GPUPipelineBase): ...

class GPUComputePipelineDescriptor(TypedDict, GPUPipelineDescriptorBase):
    compute: GPUProgrammableStage

class GPURenderPipeline(GPUObjectBase, GPUPipelineBase): ...

class GPURenderPipelineDescriptor(TypedDict, GPUPipelineDescriptorBase):
    vertex: GPUVertexState
    primitive: NotRequired[GPUPrimitiveState]
    depthStencil: NotRequired[GPUDepthStencilState]
    multisample: NotRequired[GPUMultisampleState]
    fragment: NotRequired[GPUFragmentState]

class GPUPrimitiveState(TypedDict):
    topology: NotRequired[GPUPrimitiveTopology]
    stripIndexFormat: NotRequired[GPUIndexFormat]
    frontFace: NotRequired[GPUFrontFace]
    cullMode: NotRequired[GPUCullMode]
    unclippedDepth: NotRequired[bool]

class GPUMultisampleState(TypedDict):
    count: NotRequired[GPUSize32]
    mask: NotRequired[GPUSampleMask]
    alphaToCoverageEnabled: NotRequired[bool]

class GPUFragmentState(TypedDict, GPUProgrammableStage):
    targets: Sequence[GPUColorTargetState | None]

class GPUColorTargetState(TypedDict):
    format: GPUTextureFormat
    blend: NotRequired[GPUBlendState]
    writeMask: NotRequired[GPUColorWriteFlags]

class GPUBlendState(TypedDict):
    color: GPUBlendComponent
    alpha: GPUBlendComponent

class GPUBlendComponent(TypedDict):
    operation: NotRequired[GPUBlendOperation]
    srcFactor: NotRequired[GPUBlendFactor]
    dstFactor: NotRequired[GPUBlendFactor]

class GPUDepthStencilState(TypedDict):
    format: GPUTextureFormat
    depthWriteEnabled: NotRequired[bool]
    depthCompare: NotRequired[GPUCompareFunction]
    stencilFront: NotRequired[GPUStencilFaceState]
    stencilBack: NotRequired[GPUStencilFaceState]
    stencilReadMask: NotRequired[GPUStencilValue]
    stencilWriteMask: NotRequired[GPUStencilValue]
    depthBias: NotRequired[GPUDepthBias]
    depthBiasSlopeScale: NotRequired[float]
    depthBiasClamp: NotRequired[float]

class GPUStencilFaceState(TypedDict):
    compare: NotRequired[GPUCompareFunction]
    failOp: NotRequired[GPUStencilOperation]
    depthFailOp: NotRequired[GPUStencilOperation]
    passOp: NotRequired[GPUStencilOperation]

class GPUVertexState(TypedDict, GPUProgrammableStage):
    buffers: NotRequired[Sequence[GPUVertexBufferLayout | None]]

class GPUVertexBufferLayout(TypedDict):
    arrayStride: GPUSize64
    stepMode: NotRequired[GPUVertexStepMode]
    attributes: Sequence[GPUVertexAttribute]

class GPUVertexAttribute(TypedDict):
    format: GPUVertexFormat
    offset: GPUSize64
    shaderLocation: GPUIndex32

class GPUImageDataLayout(TypedDict):
    offset: NotRequired[GPUSize64]
    bytesPerRow: NotRequired[GPUSize32]
    rowsPerImage: NotRequired[GPUSize32]

class GPUImageCopyBuffer(TypedDict, GPUImageDataLayout):
    buffer: GPUBuffer

class GPUImageCopyTexture(TypedDict):
    texture: GPUTexture
    mipLevel: NotRequired[GPUIntegerCoordinate]
    origin: NotRequired[GPUOrigin3D]
    aspect: NotRequired[GPUTextureAspect]

class GPUImageCopyTextureTagged(TypedDict, GPUImageCopyTexture):
    colorSpace: NotRequired[PredefinedColorSpace]
    premultipliedAlpha: NotRequired[bool]

class GPUImageCopyExternalImage(TypedDict):
    source: ImageBitmap | HTMLVideoElement | HTMLCanvasElement | OffscreenCanvas
    origin: NotRequired[GPUOrigin2D]
    flipY: NotRequired[bool]

class GPUCommandBuffer(GPUObjectBase): ...

class GPUCommandBufferDescriptor(TypedDict, GPUObjectDescriptorBase): ...

class GPUCommandsMixin: ...

class GPUCommandEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin):
    def beginRenderPass(self, descriptor: GPURenderPassDescriptor) -> GPURenderPassEncoder: ...
    def beginComputePass(self, descriptor: GPUComputePassDescriptor | None = {}) -> GPUComputePassEncoder: ...
    def copyBufferToBuffer(self, source: GPUBuffer, sourceOffset: GPUSize64, destination: GPUBuffer, destinationOffset: GPUSize64, size: GPUSize64): ...
    def copyBufferToTexture(self, source: GPUImageCopyBuffer, destination: GPUImageCopyTexture, copySize: GPUExtent3D): ...
    def copyTextureToBuffer(self, source: GPUImageCopyTexture, destination: GPUImageCopyBuffer, copySize: GPUExtent3D): ...
    def copyTextureToTexture(self, source: GPUImageCopyTexture, destination: GPUImageCopyTexture, copySize: GPUExtent3D): ...
    def clearBuffer(self, buffer: GPUBuffer, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def writeTimestamp(self, querySet: GPUQuerySet, queryIndex: GPUSize32): ...
    def resolveQuerySet(self, querySet: GPUQuerySet, firstQuery: GPUSize32, queryCount: GPUSize32, destination: GPUBuffer, destinationOffset: GPUSize64): ...
    def finish(self, descriptor: GPUCommandBufferDescriptor | None = {}) -> GPUCommandBuffer: ...

class GPUCommandEncoderDescriptor(TypedDict, GPUObjectDescriptorBase): ...

class GPUBindingCommandsMixin:
    @overload
    def setBindGroup(self, index: GPUIndex32, bindGroup: GPUBindGroup, dynamicOffsets: Sequence[GPUBufferDynamicOffset] | None = []): ...
    @overload
    def setBindGroup(self, index: GPUIndex32, bindGroup: GPUBindGroup, dynamicOffsetsData: Uint32Array, dynamicOffsetsDataStart: GPUSize64, dynamicOffsetsDataLength: GPUSize32): ...

class GPUDebugCommandsMixin:
    def pushDebugGroup(self, groupLabel: USVString): ...
    def popDebugGroup(self): ...
    def insertDebugMarker(self, markerLabel: USVString): ...

class GPUComputePassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin):
    def setPipeline(self, pipeline: GPUComputePipeline): ...
    def dispatchWorkgroups(self, workgroupCountX: GPUSize32, workgroupCountY: GPUSize32 | None = 1, workgroupCountZ: GPUSize32 | None = 1): ...
    def dispatchWorkgroupsIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...
    def end(self): ...

class GPUComputePassTimestampWrite(TypedDict):
    querySet: GPUQuerySet
    queryIndex: GPUSize32
    location: GPUComputePassTimestampLocation

class GPUComputePassDescriptor(TypedDict, GPUObjectDescriptorBase):
    timestampWrites: NotRequired[GPUComputePassTimestampWrites]

class GPURenderPassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin, GPURenderCommandsMixin):
    def setViewport(self, x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float): ...
    def setScissorRect(self, x: GPUIntegerCoordinate, y: GPUIntegerCoordinate, width: GPUIntegerCoordinate, height: GPUIntegerCoordinate): ...
    def setBlendConstant(self, color: GPUColor): ...
    def setStencilReference(self, reference: GPUStencilValue): ...
    def beginOcclusionQuery(self, queryIndex: GPUSize32): ...
    def endOcclusionQuery(self): ...
    def executeBundles(self, bundles: Sequence[GPURenderBundle]): ...
    def end(self): ...

class GPURenderPassTimestampWrite(TypedDict):
    querySet: GPUQuerySet
    queryIndex: GPUSize32
    location: GPURenderPassTimestampLocation

class GPURenderPassDescriptor(TypedDict, GPUObjectDescriptorBase):
    colorAttachments: Sequence[GPURenderPassColorAttachment | None]
    depthStencilAttachment: NotRequired[GPURenderPassDepthStencilAttachment]
    occlusionQuerySet: NotRequired[GPUQuerySet]
    timestampWrites: NotRequired[GPURenderPassTimestampWrites]
    maxDrawCount: NotRequired[GPUSize64]

class GPURenderPassColorAttachment(TypedDict):
    view: GPUTextureView
    resolveTarget: NotRequired[GPUTextureView]
    clearValue: NotRequired[GPUColor]
    loadOp: GPULoadOp
    storeOp: GPUStoreOp

class GPURenderPassDepthStencilAttachment(TypedDict):
    view: GPUTextureView
    depthClearValue: NotRequired[float]
    depthLoadOp: NotRequired[GPULoadOp]
    depthStoreOp: NotRequired[GPUStoreOp]
    depthReadOnly: NotRequired[bool]
    stencilClearValue: NotRequired[GPUStencilValue]
    stencilLoadOp: NotRequired[GPULoadOp]
    stencilStoreOp: NotRequired[GPUStoreOp]
    stencilReadOnly: NotRequired[bool]

class GPURenderPassLayout(TypedDict, GPUObjectDescriptorBase):
    colorFormats: Sequence[GPUTextureFormat | None]
    depthStencilFormat: NotRequired[GPUTextureFormat]
    sampleCount: NotRequired[GPUSize32]

class GPURenderCommandsMixin:
    def setPipeline(self, pipeline: GPURenderPipeline): ...
    def setIndexBuffer(self, buffer: GPUBuffer, indexFormat: GPUIndexFormat, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def setVertexBuffer(self, slot: GPUIndex32, buffer: GPUBuffer, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def draw(self, vertexCount: GPUSize32, instanceCount: GPUSize32 | None = 1, firstVertex: GPUSize32 | None = 0, firstInstance: GPUSize32 | None = 0): ...
    def drawIndexed(self, indexCount: GPUSize32, instanceCount: GPUSize32 | None = 1, firstIndex: GPUSize32 | None = 0, baseVertex: GPUSignedOffset32 | None = 0, firstInstance: GPUSize32 | None = 0): ...
    def drawIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...
    def drawIndexedIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...

class GPURenderBundle(GPUObjectBase): ...

class GPURenderBundleDescriptor(TypedDict, GPUObjectDescriptorBase): ...

class GPURenderBundleEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin, GPURenderCommandsMixin):
    def finish(self, descriptor: GPURenderBundleDescriptor | None = {}) -> GPURenderBundle: ...

class GPURenderBundleEncoderDescriptor(TypedDict, GPURenderPassLayout):
    depthReadOnly: NotRequired[bool]
    stencilReadOnly: NotRequired[bool]

class GPUQueueDescriptor(TypedDict, GPUObjectDescriptorBase): ...

class GPUQueue(GPUObjectBase):
    def submit(self, commandBuffers: Sequence[GPUCommandBuffer]): ...
    def onSubmittedWorkDone(self) -> Awaitable[None]: ...
    def writeBuffer(self, buffer: GPUBuffer, bufferOffset: GPUSize64, data: BufferSource, dataOffset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def writeTexture(self, destination: GPUImageCopyTexture, data: BufferSource, dataLayout: GPUImageDataLayout, size: GPUExtent3D): ...
    def copyExternalImageToTexture(self, source: GPUImageCopyExternalImage, destination: GPUImageCopyTextureTagged, copySize: GPUExtent3D): ...

class GPUQuerySet(GPUObjectBase):
    def destroy(self): ...
    type: GPUQueryType
    count: GPUSize32

class GPUQuerySetDescriptor(TypedDict, GPUObjectDescriptorBase):
    type: GPUQueryType
    count: GPUSize32

class GPUCanvasContext:
    canvas: HTMLCanvasElement | OffscreenCanvas
    def configure(self, configuration: GPUCanvasConfiguration): ...
    def unconfigure(self): ...
    def getCurrentTexture(self) -> GPUTexture: ...

class GPUCanvasConfiguration(TypedDict):
    device: GPUDevice
    format: GPUTextureFormat
    usage: NotRequired[GPUTextureUsageFlags]
    viewFormats: NotRequired[Sequence[GPUTextureFormat]]
    colorSpace: NotRequired[PredefinedColorSpace]
    alphaMode: NotRequired[GPUCanvasAlphaMode]

class GPUDeviceLostInfo:
    reason: GPUDeviceLostReason | None
    message: str

class GPUError:
    message: str

class GPUValidationError(GPUError):
    @classmethod
    def new(self, message: str) -> GPUValidationError: ...

class GPUOutOfMemoryError(GPUError):
    @classmethod
    def new(self, message: str) -> GPUOutOfMemoryError: ...

class GPUInternalError(GPUError):
    @classmethod
    def new(self, message: str) -> GPUInternalError: ...

class GPUUncapturedErrorEvent(Event):
    @classmethod
    def new(self, type: str, gpuUncapturedErrorEventInitDict: GPUUncapturedErrorEventInit) -> GPUUncapturedErrorEvent: ...
    error: GPUError

class GPUUncapturedErrorEventInit(TypedDict, EventInit):
    error: GPUError

class GPUColorDict(TypedDict):
    r: float
    g: float
    b: float
    a: float

class GPUOrigin2DDict(TypedDict):
    x: NotRequired[GPUIntegerCoordinate]
    y: NotRequired[GPUIntegerCoordinate]

class GPUOrigin3DDict(TypedDict):
    x: NotRequired[GPUIntegerCoordinate]
    y: NotRequired[GPUIntegerCoordinate]
    z: NotRequired[GPUIntegerCoordinate]

class GPUExtent3DDict(TypedDict):
    width: GPUIntegerCoordinate
    height: NotRequired[GPUIntegerCoordinate]
    depthOrArrayLayers: NotRequired[GPUIntegerCoordinate]

class HID(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    def getDevices(self) -> Awaitable[Sequence[HIDDevice]]: ...
    def requestDevice(self, options: HIDDeviceRequestOptions) -> Awaitable[Sequence[HIDDevice]]: ...

class HIDDeviceRequestOptions(TypedDict):
    filters: Sequence[HIDDeviceFilter]
    exclusionFilters: NotRequired[Sequence[HIDDeviceFilter]]

class HIDDeviceFilter(TypedDict):
    vendorId: NotRequired[int]
    productId: NotRequired[int]
    usagePage: NotRequired[int]
    usage: NotRequired[int]

class HIDDevice(EventTarget):
    oninputreport: EventHandler
    opened: bool
    vendorId: int
    productId: int
    productName: str
    collections: Sequence[HIDCollectionInfo]
    def open(self) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def forget(self) -> Awaitable[None]: ...
    def sendReport(self, reportId: octet, data: BufferSource) -> Awaitable[None]: ...
    def sendFeatureReport(self, reportId: octet, data: BufferSource) -> Awaitable[None]: ...
    def receiveFeatureReport(self, reportId: octet) -> Awaitable[DataView]: ...

class HIDConnectionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: HIDConnectionEventInit) -> HIDConnectionEvent: ...
    device: HIDDevice

class HIDConnectionEventInit(TypedDict, EventInit):
    device: HIDDevice

class HIDInputReportEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: HIDInputReportEventInit) -> HIDInputReportEvent: ...
    device: HIDDevice
    reportId: octet
    data: DataView

class HIDInputReportEventInit(TypedDict, EventInit):
    device: HIDDevice
    reportId: octet
    data: DataView

class HIDCollectionInfo(TypedDict):
    usagePage: NotRequired[int]
    usage: NotRequired[int]
    type: NotRequired[octet]
    children: NotRequired[Sequence[HIDCollectionInfo]]
    inputReports: NotRequired[Sequence[HIDReportInfo]]
    outputReports: NotRequired[Sequence[HIDReportInfo]]
    featureReports: NotRequired[Sequence[HIDReportInfo]]

class HIDReportInfo(TypedDict):
    reportId: NotRequired[octet]
    items: NotRequired[Sequence[HIDReportItem]]

class HIDReportItem(TypedDict):
    isAbsolute: NotRequired[bool]
    isArray: NotRequired[bool]
    isBufferedBytes: NotRequired[bool]
    isConstant: NotRequired[bool]
    isLinear: NotRequired[bool]
    isRange: NotRequired[bool]
    isVolatile: NotRequired[bool]
    hasNull: NotRequired[bool]
    hasPreferredState: NotRequired[bool]
    wrap: NotRequired[bool]
    usages: NotRequired[Sequence[int]]
    usageMinimum: NotRequired[int]
    usageMaximum: NotRequired[int]
    reportSize: NotRequired[int]
    reportCount: NotRequired[int]
    unitExponent: NotRequired[byte]
    unitSystem: NotRequired[HIDUnitSystem]
    unitFactorLengthExponent: NotRequired[byte]
    unitFactorMassExponent: NotRequired[byte]
    unitFactorTimeExponent: NotRequired[byte]
    unitFactorTemperatureExponent: NotRequired[byte]
    unitFactorCurrentExponent: NotRequired[byte]
    unitFactorLuminousIntensityExponent: NotRequired[byte]
    logicalMinimum: NotRequired[int]
    logicalMaximum: NotRequired[int]
    physicalMinimum: NotRequired[int]
    physicalMaximum: NotRequired[int]
    strings: NotRequired[Sequence[str]]

class DOMException:
    @classmethod
    def new(self, message: str | None = "", name: str | None = "Error") -> DOMException: ...
    name: str
    message: str
    code: int
    INDEX_SIZE_ERR = 1
    DOMSTRING_SIZE_ERR = 2
    HIERARCHY_REQUEST_ERR = 3
    WRONG_DOCUMENT_ERR = 4
    INVALID_CHARACTER_ERR = 5
    NO_DATA_ALLOWED_ERR = 6
    NO_MODIFICATION_ALLOWED_ERR = 7
    NOT_FOUND_ERR = 8
    NOT_SUPPORTED_ERR = 9
    INUSE_ATTRIBUTE_ERR = 10
    INVALID_STATE_ERR = 11
    SYNTAX_ERR = 12
    INVALID_MODIFICATION_ERR = 13
    NAMESPACE_ERR = 14
    INVALID_ACCESS_ERR = 15
    VALIDATION_ERR = 16
    TYPE_MISMATCH_ERR = 17
    SECURITY_ERR = 18
    NETWORK_ERR = 19
    ABORT_ERR = 20
    URL_MISMATCH_ERR = 21
    QUOTA_EXCEEDED_ERR = 22
    TIMEOUT_ERR = 23
    INVALID_NODE_TYPE_ERR = 24
    DATA_CLONE_ERR = 25

class MidiPermissionDescriptor(TypedDict, PermissionDescriptor):
    sysex: NotRequired[bool]

class MIDIOptions(TypedDict):
    sysex: NotRequired[bool]
    software: NotRequired[bool]

class MIDIInputMap: ...

class MIDIOutputMap: ...

class MIDIAccess(EventTarget):
    inputs: MIDIInputMap
    outputs: MIDIOutputMap
    onstatechange: EventHandler
    sysexEnabled: bool

class MIDIPort(EventTarget):
    id: str
    manufacturer: str | None
    name: str | None
    type: MIDIPortType
    version: str | None
    state: MIDIPortDeviceState
    connection: MIDIPortConnectionState
    onstatechange: EventHandler
    def open(self) -> Awaitable[MIDIPort]: ...
    def close(self) -> Awaitable[MIDIPort]: ...

class MIDIInput(MIDIPort):
    onmidimessage: EventHandler

class MIDIOutput(MIDIPort):
    def send(self, data: Sequence[octet], timestamp: DOMHighResTimeStamp | None = 0): ...
    def clear(self): ...

class MIDIMessageEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: MIDIMessageEventInit | None = {}) -> MIDIMessageEvent: ...
    data: Uint8Array

class MIDIMessageEventInit(TypedDict, EventInit):
    data: NotRequired[Uint8Array]

class MIDIConnectionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: MIDIConnectionEventInit | None = {}) -> MIDIConnectionEvent: ...
    port: MIDIPort

class MIDIConnectionEventInit(TypedDict, EventInit):
    port: NotRequired[MIDIPort]

class NavigatorML:
    ml: ML

class MLContextOptions(TypedDict):
    deviceType: NotRequired[MLDeviceType]
    powerPreference: NotRequired[MLPowerPreference]

class ML:
    @overload
    def createContext(self, options: MLContextOptions | None = {}) -> Awaitable[MLContext]: ...
    @overload
    def createContext(self, gpuDevice: GPUDevice) -> Awaitable[MLContext]: ...
    @overload
    def createContextSync(self, options: MLContextOptions | None = {}) -> MLContext: ...
    @overload
    def createContextSync(self, gpuDevice: GPUDevice) -> MLContext: ...

class MLGraph: ...

class MLOperandDescriptor(TypedDict):
    type: MLOperandType
    dimensions: NotRequired[Sequence[int]]

class MLOperand: ...

class MLActivation: ...

class MLContext:
    def computeSync(self, graph: MLGraph, inputs: MLNamedArrayBufferViews, outputs: MLNamedArrayBufferViews): ...
    def compute(self, graph: MLGraph, inputs: MLNamedArrayBufferViews, outputs: MLNamedArrayBufferViews) -> Awaitable[MLComputeResult]: ...
    def createCommandEncoder(self) -> MLCommandEncoder: ...

class MLComputeResult(TypedDict):
    inputs: NotRequired[MLNamedArrayBufferViews]
    outputs: NotRequired[MLNamedArrayBufferViews]

class MLCommandEncoder:
    def initializeGraph(self, graph: MLGraph): ...
    def dispatch(self, graph: MLGraph, inputs: MLNamedGPUResources, outputs: MLNamedGPUResources): ...
    def finish(self, descriptor: GPUCommandBufferDescriptor | None = {}) -> GPUCommandBuffer: ...

class MLBufferResourceView(TypedDict):
    resource: GPUBuffer
    offset: NotRequired[int]
    size: NotRequired[int]

class MLGraphBuilder:
    @classmethod
    def new(self, context: MLContext) -> MLGraphBuilder: ...
    def input(self, name: str, desc: MLOperandDescriptor) -> MLOperand: ...
    @overload
    def constant(self, desc: MLOperandDescriptor, bufferView: MLBufferView) -> MLOperand: ...
    @overload
    def constant(self, value: float, type: MLOperandType | None = "float32") -> MLOperand: ...
    def build(self, outputs: MLNamedOperands) -> Awaitable[MLGraph]: ...
    def buildSync(self, outputs: MLNamedOperands) -> MLGraph: ...
    def batchNormalization(self, input: MLOperand, mean: MLOperand, variance: MLOperand, options: MLBatchNormalizationOptions | None = {}) -> MLOperand: ...
    @overload
    def clamp(self, x: MLOperand, options: MLClampOptions | None = {}) -> MLOperand: ...
    @overload
    def clamp(self, options: MLClampOptions | None = {}) -> MLActivation: ...
    def concat(self, inputs: Sequence[MLOperand], axis: int) -> MLOperand: ...
    def conv2d(self, input: MLOperand, filter: MLOperand, options: MLConv2dOptions | None = {}) -> MLOperand: ...
    def convTranspose2d(self, input: MLOperand, filter: MLOperand, options: MLConvTranspose2dOptions | None = {}) -> MLOperand: ...
    def add(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def sub(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def mul(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def div(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def max(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def min(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def pow(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def abs(self, x: MLOperand) -> MLOperand: ...
    def ceil(self, x: MLOperand) -> MLOperand: ...
    def cos(self, x: MLOperand) -> MLOperand: ...
    def exp(self, x: MLOperand) -> MLOperand: ...
    def floor(self, x: MLOperand) -> MLOperand: ...
    def log(self, x: MLOperand) -> MLOperand: ...
    def neg(self, x: MLOperand) -> MLOperand: ...
    def sin(self, x: MLOperand) -> MLOperand: ...
    def tan(self, x: MLOperand) -> MLOperand: ...
    @overload
    def elu(self, x: MLOperand, options: MLEluOptions | None = {}) -> MLOperand: ...
    @overload
    def elu(self, options: MLEluOptions | None = {}) -> MLActivation: ...
    def gemm(self, a: MLOperand, b: MLOperand, options: MLGemmOptions | None = {}) -> MLOperand: ...
    def gru(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, steps: int, hiddenSize: int, options: MLGruOptions | None = {}) -> Sequence[MLOperand]: ...
    def gruCell(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, hiddenState: MLOperand, hiddenSize: int, options: MLGruCellOptions | None = {}) -> MLOperand: ...
    @overload
    def hardSigmoid(self, x: MLOperand, options: MLHardSigmoidOptions | None = {}) -> MLOperand: ...
    @overload
    def hardSigmoid(self, options: MLHardSigmoidOptions | None = {}) -> MLActivation: ...
    @overload
    def hardSwish(self, x: MLOperand) -> MLOperand: ...
    @overload
    def hardSwish(self) -> MLActivation: ...
    def instanceNormalization(self, input: MLOperand, options: MLInstanceNormalizationOptions | None = {}) -> MLOperand: ...
    @overload
    def leakyRelu(self, x: MLOperand, options: MLLeakyReluOptions | None = {}) -> MLOperand: ...
    @overload
    def leakyRelu(self, options: MLLeakyReluOptions | None = {}) -> MLActivation: ...
    @overload
    def linear(self, x: MLOperand, options: MLLinearOptions | None = {}) -> MLOperand: ...
    @overload
    def linear(self, options: MLLinearOptions | None = {}) -> MLActivation: ...
    def lstm(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, steps: int, hiddenSize: int, options: MLLstmOptions | None = {}) -> Sequence[MLOperand]: ...
    def lstmCell(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, hiddenState: MLOperand, cellState: MLOperand, hiddenSize: int, options: MLLstmCellOptions | None = {}) -> Sequence[MLOperand]: ...
    def matmul(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def pad(self, input: MLOperand, padding: MLOperand, options: MLPadOptions | None = {}) -> MLOperand: ...
    def averagePool2d(self, input: MLOperand, options: MLPool2dOptions | None = {}) -> MLOperand: ...
    def l2Pool2d(self, input: MLOperand, options: MLPool2dOptions | None = {}) -> MLOperand: ...
    def maxPool2d(self, input: MLOperand, options: MLPool2dOptions | None = {}) -> MLOperand: ...
    def reduceL1(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceL2(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceLogSum(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceLogSumExp(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceMax(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceMean(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceMin(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceProduct(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceSum(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceSumSquare(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    @overload
    def relu(self, x: MLOperand) -> MLOperand: ...
    @overload
    def relu(self) -> MLActivation: ...
    def resample2d(self, input: MLOperand, options: MLResample2dOptions | None = {}) -> MLOperand: ...
    def reshape(self, input: MLOperand, newShape: Sequence[int | None]) -> MLOperand: ...
    @overload
    def sigmoid(self, x: MLOperand) -> MLOperand: ...
    @overload
    def sigmoid(self) -> MLActivation: ...
    def slice(self, input: MLOperand, starts: Sequence[int], sizes: Sequence[int], options: MLSliceOptions | None = {}) -> MLOperand: ...
    @overload
    def softmax(self, x: MLOperand) -> MLOperand: ...
    @overload
    def softmax(self) -> MLActivation: ...
    @overload
    def softplus(self, x: MLOperand, options: MLSoftplusOptions | None = {}) -> MLOperand: ...
    @overload
    def softplus(self, options: MLSoftplusOptions | None = {}) -> MLActivation: ...
    @overload
    def softsign(self, x: MLOperand) -> MLOperand: ...
    @overload
    def softsign(self) -> MLActivation: ...
    def split(self, input: MLOperand, splits: int | Sequence[int], options: MLSplitOptions | None = {}) -> Sequence[MLOperand]: ...
    def squeeze(self, input: MLOperand, options: MLSqueezeOptions | None = {}) -> MLOperand: ...
    @overload
    def tanh(self, x: MLOperand) -> MLOperand: ...
    @overload
    def tanh(self) -> MLActivation: ...
    def transpose(self, input: MLOperand, options: MLTransposeOptions | None = {}) -> MLOperand: ...

class MLBatchNormalizationOptions(TypedDict):
    scale: NotRequired[MLOperand]
    bias: NotRequired[MLOperand]
    axis: NotRequired[int]
    epsilon: NotRequired[float]
    activation: NotRequired[MLActivation]

class MLClampOptions(TypedDict):
    minValue: NotRequired[float]
    maxValue: NotRequired[float]

class MLConv2dOptions(TypedDict):
    padding: NotRequired[Sequence[int]]
    strides: NotRequired[Sequence[int]]
    dilations: NotRequired[Sequence[int]]
    autoPad: NotRequired[MLAutoPad]
    groups: NotRequired[int]
    inputLayout: NotRequired[MLInputOperandLayout]
    filterLayout: NotRequired[MLConv2dFilterOperandLayout]
    bias: NotRequired[MLOperand]
    activation: NotRequired[MLActivation]

class MLConvTranspose2dOptions(TypedDict):
    padding: NotRequired[Sequence[int]]
    strides: NotRequired[Sequence[int]]
    dilations: NotRequired[Sequence[int]]
    outputPadding: NotRequired[Sequence[int]]
    outputSizes: NotRequired[Sequence[int]]
    autoPad: NotRequired[MLAutoPad]
    groups: NotRequired[int]
    inputLayout: NotRequired[MLInputOperandLayout]
    filterLayout: NotRequired[MLConvTranspose2dFilterOperandLayout]
    bias: NotRequired[MLOperand]
    activation: NotRequired[MLActivation]

class MLEluOptions(TypedDict):
    alpha: NotRequired[float]

class MLGemmOptions(TypedDict):
    c: NotRequired[MLOperand]
    alpha: NotRequired[float]
    beta: NotRequired[float]
    aTranspose: NotRequired[bool]
    bTranspose: NotRequired[bool]

class MLGruOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    initialHiddenState: NotRequired[MLOperand]
    resetAfter: NotRequired[bool]
    returnSequence: NotRequired[bool]
    direction: NotRequired[MLRecurrentNetworkDirection]
    layout: NotRequired[MLGruWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLGruCellOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    resetAfter: NotRequired[bool]
    layout: NotRequired[MLGruWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLHardSigmoidOptions(TypedDict):
    alpha: NotRequired[float]
    beta: NotRequired[float]

class MLInstanceNormalizationOptions(TypedDict):
    scale: NotRequired[MLOperand]
    bias: NotRequired[MLOperand]
    epsilon: NotRequired[float]
    layout: NotRequired[MLInputOperandLayout]

class MLLeakyReluOptions(TypedDict):
    alpha: NotRequired[float]

class MLLinearOptions(TypedDict):
    alpha: NotRequired[float]
    beta: NotRequired[float]

class MLLstmOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    peepholeWeight: NotRequired[MLOperand]
    initialHiddenState: NotRequired[MLOperand]
    initialCellState: NotRequired[MLOperand]
    returnSequence: NotRequired[bool]
    direction: NotRequired[MLRecurrentNetworkDirection]
    layout: NotRequired[MLLstmWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLLstmCellOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    peepholeWeight: NotRequired[MLOperand]
    layout: NotRequired[MLLstmWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLPadOptions(TypedDict):
    mode: NotRequired[MLPaddingMode]
    value: NotRequired[float]

class MLPool2dOptions(TypedDict):
    windowDimensions: NotRequired[Sequence[int]]
    padding: NotRequired[Sequence[int]]
    strides: NotRequired[Sequence[int]]
    dilations: NotRequired[Sequence[int]]
    autoPad: NotRequired[MLAutoPad]
    layout: NotRequired[MLInputOperandLayout]
    roundingType: NotRequired[MLRoundingType]
    outputSizes: NotRequired[Sequence[int]]

class MLReduceOptions(TypedDict):
    axes: NotRequired[Sequence[int]]
    keepDimensions: NotRequired[bool]

class MLResample2dOptions(TypedDict):
    mode: NotRequired[MLInterpolationMode]
    scales: NotRequired[Sequence[float]]
    sizes: NotRequired[Sequence[int]]
    axes: NotRequired[Sequence[int]]

class MLSliceOptions(TypedDict):
    axes: NotRequired[Sequence[int]]

class MLSoftplusOptions(TypedDict):
    steepness: NotRequired[float]

class MLSplitOptions(TypedDict):
    axis: NotRequired[int]

class MLSqueezeOptions(TypedDict):
    axes: NotRequired[Sequence[int]]

class MLTransposeOptions(TypedDict):
    permutation: NotRequired[Sequence[int]]

class RTCRtpSender:
    transform: RTCRtpTransform | None
    def generateKeyFrame(self, rids: Sequence[str] | None = None) -> Awaitable[None]: ...
    track: MediaStreamTrack | None
    transport: RTCDtlsTransport | None
    def setParameters(self, parameters: RTCRtpSendParameters) -> Awaitable[None]: ...
    def getParameters(self) -> RTCRtpSendParameters: ...
    def replaceTrack(self, withTrack: MediaStreamTrack | None) -> Awaitable[None]: ...
    def setStreams(self, *streams: MediaStream): ...
    def getStats(self) -> Awaitable[RTCStatsReport]: ...
    dtmf: RTCDTMFSender | None

class RTCRtpReceiver:
    transform: RTCRtpTransform | None
    track: MediaStreamTrack
    transport: RTCDtlsTransport | None
    def getParameters(self) -> RTCRtpReceiveParameters: ...
    def getContributingSources(self) -> Sequence[RTCRtpContributingSource]: ...
    def getSynchronizationSources(self) -> Sequence[RTCRtpSynchronizationSource]: ...
    def getStats(self) -> Awaitable[RTCStatsReport]: ...

class SFrameTransformOptions(TypedDict):
    role: NotRequired[SFrameTransformRole]

class SFrameTransform(GenericTransformStream):
    @classmethod
    def new(self, options: SFrameTransformOptions | None = {}) -> SFrameTransform: ...
    def setEncryptionKey(self, key: CryptoKey, keyID: CryptoKeyID | None = None) -> Awaitable[None]: ...
    onerror: EventHandler

class SFrameTransformErrorEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: SFrameTransformErrorEventInit) -> SFrameTransformErrorEvent: ...
    errorType: SFrameTransformErrorEventType
    keyID: CryptoKeyID | None
    frame: Any

class SFrameTransformErrorEventInit(TypedDict, EventInit):
    errorType: SFrameTransformErrorEventType
    frame: Any
    keyID: NotRequired[CryptoKeyID | None]

class RTCEncodedVideoFrameMetadata(TypedDict):
    frameId: NotRequired[int]
    dependencies: NotRequired[Sequence[int]]
    width: NotRequired[int]
    height: NotRequired[int]
    spatialIndex: NotRequired[int]
    temporalIndex: NotRequired[int]
    synchronizationSource: NotRequired[int]
    payloadType: NotRequired[octet]
    contributingSources: NotRequired[Sequence[int]]

class RTCEncodedVideoFrame:
    type: RTCEncodedVideoFrameType
    timestamp: int
    data: ArrayBuffer
    def getMetadata(self) -> RTCEncodedVideoFrameMetadata: ...

class RTCEncodedAudioFrameMetadata(TypedDict):
    synchronizationSource: NotRequired[int]
    payloadType: NotRequired[octet]
    contributingSources: NotRequired[Sequence[int]]

class RTCEncodedAudioFrame:
    timestamp: int
    data: ArrayBuffer
    def getMetadata(self) -> RTCEncodedAudioFrameMetadata: ...

class RTCTransformEvent(Event):
    transformer: RTCRtpScriptTransformer

class RTCRtpScriptTransformer:
    readable: ReadableStream
    writable: WritableStream
    options: Any
    def generateKeyFrame(self, rid: str | None = None) -> Awaitable[int]: ...
    def sendKeyFrameRequest(self) -> Awaitable[None]: ...

class RTCRtpScriptTransform:
    @classmethod
    def new(self, worker: Worker, options: Any | None = None, transfer: Sequence[object] | None = None) -> RTCRtpScriptTransform: ...

class RTCIceParameters(TypedDict, TypedDict):
    iceLite: NotRequired[bool]
    usernameFragment: NotRequired[str]
    password: NotRequired[str]

class RTCIceGatherOptions(TypedDict):
    gatherPolicy: NotRequired[RTCIceTransportPolicy]
    iceServers: NotRequired[Sequence[RTCIceServer]]

class RTCIceTransport(EventTarget):
    @classmethod
    def new(self) -> RTCIceTransport: ...
    def gather(self, options: RTCIceGatherOptions | None = {}): ...
    def start(self, remoteParameters: RTCIceParameters | None = {}, role: RTCIceRole | None = "controlled"): ...
    def stop(self): ...
    def addRemoteCandidate(self, remoteCandidate: RTCIceCandidateInit | None = {}): ...
    onerror: EventHandler
    onicecandidate: EventHandler
    role: RTCIceRole
    component: RTCIceComponent
    state: RTCIceTransportState
    gatheringState: RTCIceGathererState
    def getLocalCandidates(self) -> Sequence[RTCIceCandidate]: ...
    def getRemoteCandidates(self) -> Sequence[RTCIceCandidate]: ...
    def getSelectedCandidatePair(self) -> RTCIceCandidatePair | None: ...
    def getLocalParameters(self) -> RTCIceParameters | None: ...
    def getRemoteParameters(self) -> RTCIceParameters | None: ...
    onstatechange: EventHandler
    ongatheringstatechange: EventHandler
    onselectedcandidatepairchange: EventHandler

class RTCIdentityProviderGlobalScope(WorkerGlobalScope):
    rtcIdentityProvider: RTCIdentityProviderRegistrar

class RTCIdentityProviderRegistrar:
    def register(self, idp: RTCIdentityProvider): ...

class RTCIdentityProvider(TypedDict):
    generateAssertion: GenerateAssertionCallback
    validateAssertion: ValidateAssertionCallback

class RTCIdentityAssertionResult(TypedDict):
    idp: RTCIdentityProviderDetails
    assertion: str

class RTCIdentityProviderDetails(TypedDict):
    domain: str
    protocol: NotRequired[str]

class RTCIdentityValidationResult(TypedDict):
    identity: str
    contents: str

class RTCPeerConnection(EventTarget):
    @classmethod
    def new(self, configuration: RTCConfiguration | None = {}) -> RTCPeerConnection: ...
    def setIdentityProvider(self, provider: str, options: RTCIdentityProviderOptions | None = {}): ...
    def getIdentityAssertion(self) -> Awaitable[str]: ...
    peerIdentity: Awaitable[RTCIdentityAssertion]
    idpLoginUrl: str | None
    idpErrorInfo: str | None
    @overload
    def createOffer(self, options: RTCOfferOptions | None = {}) -> Awaitable[RTCSessionDescriptionInit]: ...
    @overload
    def createAnswer(self, options: RTCAnswerOptions | None = {}) -> Awaitable[RTCSessionDescriptionInit]: ...
    @overload
    def setLocalDescription(self, description: RTCLocalSessionDescriptionInit | None = {}) -> Awaitable[None]: ...
    localDescription: RTCSessionDescription | None
    currentLocalDescription: RTCSessionDescription | None
    pendingLocalDescription: RTCSessionDescription | None
    @overload
    def setRemoteDescription(self, description: RTCSessionDescriptionInit) -> Awaitable[None]: ...
    remoteDescription: RTCSessionDescription | None
    currentRemoteDescription: RTCSessionDescription | None
    pendingRemoteDescription: RTCSessionDescription | None
    @overload
    def addIceCandidate(self, candidate: RTCIceCandidateInit | None = {}) -> Awaitable[None]: ...
    signalingState: RTCSignalingState
    iceGatheringState: RTCIceGatheringState
    iceConnectionState: RTCIceConnectionState
    connectionState: RTCPeerConnectionState
    canTrickleIceCandidates: bool | None
    def restartIce(self): ...
    def getConfiguration(self) -> RTCConfiguration: ...
    def setConfiguration(self, configuration: RTCConfiguration | None = {}): ...
    def close(self): ...
    onnegotiationneeded: EventHandler
    onicecandidate: EventHandler
    onicecandidateerror: EventHandler
    onsignalingstatechange: EventHandler
    oniceconnectionstatechange: EventHandler
    onicegatheringstatechange: EventHandler
    onconnectionstatechange: EventHandler
    @overload
    def createOffer(self, successCallback: RTCSessionDescriptionCallback, failureCallback: RTCPeerConnectionErrorCallback, options: RTCOfferOptions | None = {}) -> Awaitable[None]: ...
    @overload
    def setLocalDescription(self, description: RTCLocalSessionDescriptionInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def createAnswer(self, successCallback: RTCSessionDescriptionCallback, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def setRemoteDescription(self, description: RTCSessionDescriptionInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def addIceCandidate(self, candidate: RTCIceCandidateInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    def getSenders(self) -> Sequence[RTCRtpSender]: ...
    def getReceivers(self) -> Sequence[RTCRtpReceiver]: ...
    def getTransceivers(self) -> Sequence[RTCRtpTransceiver]: ...
    def addTrack(self, track: MediaStreamTrack, *streams: MediaStream) -> RTCRtpSender: ...
    def removeTrack(self, sender: RTCRtpSender): ...
    def addTransceiver(self, trackOrKind: MediaStreamTrack | str, init: RTCRtpTransceiverInit | None = {}) -> RTCRtpTransceiver: ...
    ontrack: EventHandler
    sctp: RTCSctpTransport | None
    def createDataChannel(self, label: USVString, dataChannelDict: RTCDataChannelInit | None = {}) -> RTCDataChannel: ...
    ondatachannel: EventHandler
    def getStats(self, selector: MediaStreamTrack | None = None) -> Awaitable[RTCStatsReport]: ...

class RTCConfiguration(TypedDict, TypedDict):
    peerIdentity: NotRequired[str]
    iceServers: NotRequired[Sequence[RTCIceServer]]
    iceTransportPolicy: NotRequired[RTCIceTransportPolicy]
    bundlePolicy: NotRequired[RTCBundlePolicy]
    rtcpMuxPolicy: NotRequired[RTCRtcpMuxPolicy]
    certificates: NotRequired[Sequence[RTCCertificate]]
    iceCandidatePoolSize: NotRequired[octet]

class RTCIdentityProviderOptions(TypedDict):
    protocol: NotRequired[str]
    usernameHint: NotRequired[str]
    peerIdentity: NotRequired[str]

class RTCIdentityAssertion:
    @classmethod
    def new(self, idp: str, name: str) -> RTCIdentityAssertion: ...
    idp: str
    name: str

class RTCError(DOMException):
    @classmethod
    def new(self, init: RTCErrorInit, message: str | None = "") -> RTCError: ...
    httpRequestStatusCode: int | None
    errorDetail: RTCErrorDetailType
    sdpLineNumber: int | None
    sctpCauseCode: int | None
    receivedAlert: int | None
    sentAlert: int | None

class RTCErrorInit(TypedDict, TypedDict):
    httpRequestStatusCode: NotRequired[int]
    errorDetail: RTCErrorDetailType
    sdpLineNumber: NotRequired[int]
    sctpCauseCode: NotRequired[int]
    receivedAlert: NotRequired[int]
    sentAlert: NotRequired[int]

class RTCRtpEncodingParameters(TypedDict, TypedDict, TypedDict, RTCRtpCodingParameters):
    priority: NotRequired[RTCPriorityType]
    networkPriority: NotRequired[RTCPriorityType]
    scalabilityMode: NotRequired[str]
    active: NotRequired[bool]
    maxBitrate: NotRequired[int]
    maxFramerate: NotRequired[float]
    scaleResolutionDownBy: NotRequired[float]

class RTCDataChannel(EventTarget):
    priority: RTCPriorityType
    label: USVString
    ordered: bool
    maxPacketLifeTime: int | None
    maxRetransmits: int | None
    protocol: USVString
    negotiated: bool
    id: int | None
    readyState: RTCDataChannelState
    bufferedAmount: int
    bufferedAmountLowThreshold: int
    onopen: EventHandler
    onbufferedamountlow: EventHandler
    onerror: EventHandler
    onclosing: EventHandler
    onclose: EventHandler
    def close(self): ...
    onmessage: EventHandler
    binaryType: BinaryType
    @overload
    def send(self, data: USVString): ...
    @overload
    def send(self, data: Blob): ...
    @overload
    def send(self, data: ArrayBuffer): ...
    @overload
    def send(self, data: ArrayBufferView): ...

class RTCDataChannelInit(TypedDict, TypedDict):
    priority: NotRequired[RTCPriorityType]
    ordered: NotRequired[bool]
    maxPacketLifeTime: NotRequired[int]
    maxRetransmits: NotRequired[int]
    protocol: NotRequired[USVString]
    negotiated: NotRequired[bool]
    id: NotRequired[int]

class RTCRtpStreamStats(TypedDict, RTCStats):
    ssrc: int
    kind: str
    transportId: NotRequired[str]
    codecId: NotRequired[str]

class RTCCodecStats(TypedDict, RTCStats):
    payloadType: int
    transportId: str
    mimeType: str
    clockRate: NotRequired[int]
    channels: NotRequired[int]
    sdpFmtpLine: NotRequired[str]

class RTCReceivedRtpStreamStats(TypedDict, RTCRtpStreamStats):
    packetsReceived: NotRequired[int]
    packetsLost: NotRequired[int]
    jitter: NotRequired[float]

class RTCInboundRtpStreamStats(TypedDict, RTCReceivedRtpStreamStats):
    trackIdentifier: str
    kind: str
    mid: NotRequired[str]
    remoteId: NotRequired[str]
    framesDecoded: NotRequired[int]
    keyFramesDecoded: NotRequired[int]
    framesRendered: NotRequired[int]
    framesDropped: NotRequired[int]
    frameWidth: NotRequired[int]
    frameHeight: NotRequired[int]
    framesPerSecond: NotRequired[float]
    qpSum: NotRequired[int]
    totalDecodeTime: NotRequired[float]
    totalInterFrameDelay: NotRequired[float]
    totalSquaredInterFrameDelay: NotRequired[float]
    pauseCount: NotRequired[int]
    totalPausesDuration: NotRequired[float]
    freezeCount: NotRequired[int]
    totalFreezesDuration: NotRequired[float]
    lastPacketReceivedTimestamp: NotRequired[DOMHighResTimeStamp]
    headerBytesReceived: NotRequired[int]
    packetsDiscarded: NotRequired[int]
    fecPacketsReceived: NotRequired[int]
    fecPacketsDiscarded: NotRequired[int]
    bytesReceived: NotRequired[int]
    nackCount: NotRequired[int]
    firCount: NotRequired[int]
    pliCount: NotRequired[int]
    totalProcessingDelay: NotRequired[float]
    estimatedPlayoutTimestamp: NotRequired[DOMHighResTimeStamp]
    jitterBufferDelay: NotRequired[float]
    jitterBufferTargetDelay: NotRequired[float]
    jitterBufferEmittedCount: NotRequired[int]
    jitterBufferMinimumDelay: NotRequired[float]
    totalSamplesReceived: NotRequired[int]
    concealedSamples: NotRequired[int]
    silentConcealedSamples: NotRequired[int]
    concealmentEvents: NotRequired[int]
    insertedSamplesForDeceleration: NotRequired[int]
    removedSamplesForAcceleration: NotRequired[int]
    audioLevel: NotRequired[float]
    totalAudioEnergy: NotRequired[float]
    totalSamplesDuration: NotRequired[float]
    framesReceived: NotRequired[int]
    decoderImplementation: NotRequired[str]
    playoutId: NotRequired[str]
    powerEfficientDecoder: NotRequired[bool]
    framesAssembledFromMultiplePackets: NotRequired[int]
    totalAssemblyTime: NotRequired[float]

class RTCRemoteInboundRtpStreamStats(TypedDict, RTCReceivedRtpStreamStats):
    localId: NotRequired[str]
    roundTripTime: NotRequired[float]
    totalRoundTripTime: NotRequired[float]
    fractionLost: NotRequired[float]
    roundTripTimeMeasurements: NotRequired[int]

class RTCSentRtpStreamStats(TypedDict, RTCRtpStreamStats):
    packetsSent: NotRequired[int]
    bytesSent: NotRequired[int]

class RTCOutboundRtpStreamStats(TypedDict, RTCSentRtpStreamStats):
    mid: NotRequired[str]
    mediaSourceId: NotRequired[str]
    remoteId: NotRequired[str]
    rid: NotRequired[str]
    headerBytesSent: NotRequired[int]
    retransmittedPacketsSent: NotRequired[int]
    retransmittedBytesSent: NotRequired[int]
    targetBitrate: NotRequired[float]
    totalEncodedBytesTarget: NotRequired[int]
    frameWidth: NotRequired[int]
    frameHeight: NotRequired[int]
    framesPerSecond: NotRequired[float]
    framesSent: NotRequired[int]
    hugeFramesSent: NotRequired[int]
    framesEncoded: NotRequired[int]
    keyFramesEncoded: NotRequired[int]
    qpSum: NotRequired[int]
    totalEncodeTime: NotRequired[float]
    totalPacketSendDelay: NotRequired[float]
    qualityLimitationReason: NotRequired[RTCQualityLimitationReason]
    qualityLimitationDurations: NotRequired[float]
    qualityLimitationResolutionChanges: NotRequired[int]
    nackCount: NotRequired[int]
    firCount: NotRequired[int]
    pliCount: NotRequired[int]
    encoderImplementation: NotRequired[str]
    powerEfficientEncoder: NotRequired[bool]
    active: NotRequired[bool]
    scalabilityMode: NotRequired[str]

class RTCRemoteOutboundRtpStreamStats(TypedDict, RTCSentRtpStreamStats):
    localId: NotRequired[str]
    remoteTimestamp: NotRequired[DOMHighResTimeStamp]
    reportsSent: NotRequired[int]
    roundTripTime: NotRequired[float]
    totalRoundTripTime: NotRequired[float]
    roundTripTimeMeasurements: NotRequired[int]

class RTCMediaSourceStats(TypedDict, RTCStats):
    trackIdentifier: str
    kind: str

class RTCAudioSourceStats(TypedDict, RTCMediaSourceStats):
    audioLevel: NotRequired[float]
    totalAudioEnergy: NotRequired[float]
    totalSamplesDuration: NotRequired[float]
    echoReturnLoss: NotRequired[float]
    echoReturnLossEnhancement: NotRequired[float]
    droppedSamplesDuration: NotRequired[float]
    droppedSamplesEvents: NotRequired[int]
    totalCaptureDelay: NotRequired[float]
    totalSamplesCaptured: NotRequired[int]

class RTCVideoSourceStats(TypedDict, RTCMediaSourceStats):
    width: NotRequired[int]
    height: NotRequired[int]
    frames: NotRequired[int]
    framesPerSecond: NotRequired[float]

class RTCAudioPlayoutStats(TypedDict, RTCStats):
    synthesizedSamplesDuration: NotRequired[float]
    synthesizedSamplesEvents: NotRequired[int]
    totalSamplesDuration: NotRequired[float]
    totalPlayoutDelay: NotRequired[float]
    totalSamplesCount: NotRequired[int]

class RTCPeerConnectionStats(TypedDict, RTCStats):
    dataChannelsOpened: NotRequired[int]
    dataChannelsClosed: NotRequired[int]

class RTCDataChannelStats(TypedDict, RTCStats):
    label: NotRequired[str]
    protocol: NotRequired[str]
    dataChannelIdentifier: NotRequired[int]
    state: RTCDataChannelState
    messagesSent: NotRequired[int]
    bytesSent: NotRequired[int]
    messagesReceived: NotRequired[int]
    bytesReceived: NotRequired[int]

class RTCTransportStats(TypedDict, RTCStats):
    packetsSent: NotRequired[int]
    packetsReceived: NotRequired[int]
    bytesSent: NotRequired[int]
    bytesReceived: NotRequired[int]
    iceRole: NotRequired[RTCIceRole]
    iceLocalUsernameFragment: NotRequired[str]
    dtlsState: RTCDtlsTransportState
    iceState: NotRequired[RTCIceTransportState]
    selectedCandidatePairId: NotRequired[str]
    localCertificateId: NotRequired[str]
    remoteCertificateId: NotRequired[str]
    tlsVersion: NotRequired[str]
    dtlsCipher: NotRequired[str]
    dtlsRole: NotRequired[RTCDtlsRole]
    srtpCipher: NotRequired[str]
    selectedCandidatePairChanges: NotRequired[int]

class RTCIceCandidateStats(TypedDict, RTCStats):
    transportId: str
    address: NotRequired[str | None]
    port: NotRequired[int]
    protocol: NotRequired[str]
    candidateType: RTCIceCandidateType
    priority: NotRequired[int]
    url: NotRequired[str]
    relayProtocol: NotRequired[RTCIceServerTransportProtocol]
    foundation: NotRequired[str]
    relatedAddress: NotRequired[str]
    relatedPort: NotRequired[int]
    usernameFragment: NotRequired[str]
    tcpType: NotRequired[RTCIceTcpCandidateType]

class RTCIceCandidatePairStats(TypedDict, RTCStats):
    transportId: str
    localCandidateId: str
    remoteCandidateId: str
    state: RTCStatsIceCandidatePairState
    nominated: NotRequired[bool]
    packetsSent: NotRequired[int]
    packetsReceived: NotRequired[int]
    bytesSent: NotRequired[int]
    bytesReceived: NotRequired[int]
    lastPacketSentTimestamp: NotRequired[DOMHighResTimeStamp]
    lastPacketReceivedTimestamp: NotRequired[DOMHighResTimeStamp]
    totalRoundTripTime: NotRequired[float]
    currentRoundTripTime: NotRequired[float]
    availableOutgoingBitrate: NotRequired[float]
    availableIncomingBitrate: NotRequired[float]
    requestsReceived: NotRequired[int]
    requestsSent: NotRequired[int]
    responsesReceived: NotRequired[int]
    responsesSent: NotRequired[int]
    consentRequestsSent: NotRequired[int]
    packetsDiscardedOnSend: NotRequired[int]
    bytesDiscardedOnSend: NotRequired[int]

class RTCCertificateStats(TypedDict, RTCStats):
    fingerprint: str
    fingerprintAlgorithm: str
    base64Certificate: str
    issuerCertificateId: NotRequired[str]

class RTCRtpCodecCapability(TypedDict, TypedDict):
    scalabilityModes: NotRequired[Sequence[str]]
    mimeType: str
    clockRate: int
    channels: NotRequired[int]
    sdpFmtpLine: NotRequired[str]

class RTCIceServer(TypedDict):
    urls: str | Sequence[str]
    username: NotRequired[str]
    credential: NotRequired[str]

class RTCOfferAnswerOptions(TypedDict): ...

class RTCOfferOptions(TypedDict, RTCOfferAnswerOptions, TypedDict):
    iceRestart: NotRequired[bool]
    offerToReceiveAudio: NotRequired[bool]
    offerToReceiveVideo: NotRequired[bool]

class RTCAnswerOptions(TypedDict, RTCOfferAnswerOptions): ...

class RTCSessionDescription:
    @classmethod
    def new(self, descriptionInitDict: RTCSessionDescriptionInit) -> RTCSessionDescription: ...
    type: RTCSdpType
    sdp: str
    def toJSON(self) -> object: ...

class RTCSessionDescriptionInit(TypedDict):
    type: RTCSdpType
    sdp: NotRequired[str]

class RTCLocalSessionDescriptionInit(TypedDict):
    type: NotRequired[RTCSdpType]
    sdp: NotRequired[str]

class RTCIceCandidate:
    @classmethod
    def new(self, candidateInitDict: RTCIceCandidateInit | None = {}) -> RTCIceCandidate: ...
    candidate: str
    sdpMid: str | None
    sdpMLineIndex: int | None
    foundation: str | None
    component: RTCIceComponent | None
    priority: int | None
    address: str | None
    protocol: RTCIceProtocol | None
    port: int | None
    type: RTCIceCandidateType | None
    tcpType: RTCIceTcpCandidateType | None
    relatedAddress: str | None
    relatedPort: int | None
    usernameFragment: str | None
    relayProtocol: RTCIceServerTransportProtocol | None
    url: str | None
    def toJSON(self) -> RTCIceCandidateInit: ...

class RTCIceCandidateInit(TypedDict):
    candidate: NotRequired[str]
    sdpMid: NotRequired[str | None]
    sdpMLineIndex: NotRequired[int | None]
    usernameFragment: NotRequired[str | None]

class RTCPeerConnectionIceEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: RTCPeerConnectionIceEventInit | None = {}) -> RTCPeerConnectionIceEvent: ...
    candidate: RTCIceCandidate | None
    url: str | None

class RTCPeerConnectionIceEventInit(TypedDict, EventInit):
    candidate: NotRequired[RTCIceCandidate | None]
    url: NotRequired[str | None]

class RTCPeerConnectionIceErrorEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: RTCPeerConnectionIceErrorEventInit) -> RTCPeerConnectionIceErrorEvent: ...
    address: str | None
    port: int | None
    url: str
    errorCode: int
    errorText: USVString

class RTCPeerConnectionIceErrorEventInit(TypedDict, EventInit):
    address: NotRequired[str | None]
    port: NotRequired[int | None]
    url: NotRequired[str]
    errorCode: int
    errorText: NotRequired[USVString]

class RTCCertificateExpiration(TypedDict):
    expires: NotRequired[int]

class RTCCertificate:
    expires: EpochTimeStamp
    def getFingerprints(self) -> Sequence[RTCDtlsFingerprint]: ...

class RTCRtpTransceiverInit(TypedDict):
    direction: NotRequired[RTCRtpTransceiverDirection]
    streams: NotRequired[Sequence[MediaStream]]
    sendEncodings: NotRequired[Sequence[RTCRtpEncodingParameters]]

class RTCRtpParameters(TypedDict):
    headerExtensions: Sequence[RTCRtpHeaderExtensionParameters]
    rtcp: RTCRtcpParameters
    codecs: Sequence[RTCRtpCodecParameters]

class RTCRtpReceiveParameters(TypedDict, RTCRtpParameters): ...

class RTCRtpCodingParameters(TypedDict):
    rid: NotRequired[str]

class RTCRtcpParameters(TypedDict):
    cname: NotRequired[str]
    reducedSize: NotRequired[bool]

class RTCRtpHeaderExtensionParameters(TypedDict):
    uri: str
    id: int
    encrypted: NotRequired[bool]

class RTCRtpCodecParameters(TypedDict):
    payloadType: octet
    mimeType: str
    clockRate: int
    channels: NotRequired[int]
    sdpFmtpLine: NotRequired[str]

class RTCRtpCapabilities(TypedDict):
    codecs: Sequence[RTCRtpCodecCapability]
    headerExtensions: Sequence[RTCRtpHeaderExtensionCapability]

class RTCRtpHeaderExtensionCapability(TypedDict):
    uri: NotRequired[str]

class RTCRtpContributingSource(TypedDict):
    timestamp: DOMHighResTimeStamp
    source: int
    audioLevel: NotRequired[float]
    rtpTimestamp: int

class RTCRtpSynchronizationSource(TypedDict, RTCRtpContributingSource): ...

class RTCRtpTransceiver:
    mid: str | None
    sender: RTCRtpSender
    receiver: RTCRtpReceiver
    direction: RTCRtpTransceiverDirection
    currentDirection: RTCRtpTransceiverDirection | None
    def stop(self): ...
    def setCodecPreferences(self, codecs: Sequence[RTCRtpCodecCapability]): ...

class RTCDtlsTransport(EventTarget):
    iceTransport: RTCIceTransport
    state: RTCDtlsTransportState
    def getRemoteCertificates(self) -> Sequence[ArrayBuffer]: ...
    onstatechange: EventHandler
    onerror: EventHandler

class RTCDtlsFingerprint(TypedDict):
    algorithm: NotRequired[str]
    value: NotRequired[str]

class RTCIceCandidatePair(TypedDict):
    local: NotRequired[RTCIceCandidate]
    remote: NotRequired[RTCIceCandidate]

class RTCTrackEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: RTCTrackEventInit) -> RTCTrackEvent: ...
    receiver: RTCRtpReceiver
    track: MediaStreamTrack
    streams: Sequence[MediaStream]
    transceiver: RTCRtpTransceiver

class RTCTrackEventInit(TypedDict, EventInit):
    receiver: RTCRtpReceiver
    track: MediaStreamTrack
    streams: NotRequired[Sequence[MediaStream]]
    transceiver: RTCRtpTransceiver

class RTCSctpTransport(EventTarget):
    transport: RTCDtlsTransport
    state: RTCSctpTransportState
    maxMessageSize: float
    maxChannels: int | None
    onstatechange: EventHandler

class RTCDataChannelEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: RTCDataChannelEventInit) -> RTCDataChannelEvent: ...
    channel: RTCDataChannel

class RTCDataChannelEventInit(TypedDict, EventInit):
    channel: RTCDataChannel

class RTCDTMFSender(EventTarget):
    def insertDTMF(self, tones: str, duration: int | None = 100, interToneGap: int | None = 70): ...
    ontonechange: EventHandler
    canInsertDTMF: bool
    toneBuffer: str

class RTCDTMFToneChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: RTCDTMFToneChangeEventInit | None = {}) -> RTCDTMFToneChangeEvent: ...
    tone: str

class RTCDTMFToneChangeEventInit(TypedDict, EventInit):
    tone: NotRequired[str]

class RTCStatsReport: ...

class RTCStats(TypedDict):
    timestamp: DOMHighResTimeStamp
    type: RTCStatsType
    id: str

class RTCErrorEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: RTCErrorEventInit) -> RTCErrorEvent: ...
    error: RTCError

class RTCErrorEventInit(TypedDict, EventInit):
    error: RTCError

class WebSocket(EventTarget):
    @classmethod
    def new(self, url: USVString, protocols: str | Sequence[str] | None = []) -> WebSocket: ...
    url: USVString
    CONNECTING = 0
    OPEN = 1
    CLOSING = 2
    CLOSED = 3
    readyState: int
    bufferedAmount: int
    onopen: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    extensions: str
    protocol: str
    def close(self, code: int | None = None, reason: USVString | None = None): ...
    onmessage: EventHandler
    binaryType: BinaryType
    def send(self, data: BufferSource | Blob | USVString): ...

class CloseEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: CloseEventInit | None = {}) -> CloseEvent: ...
    wasClean: bool
    code: int
    reason: USVString

class CloseEventInit(TypedDict, EventInit):
    wasClean: NotRequired[bool]
    code: NotRequired[int]
    reason: NotRequired[USVString]

class WebTransportDatagramDuplexStream:
    readable: ReadableStream
    writable: WritableStream
    maxDatagramSize: int
    incomingMaxAge: float | None
    outgoingMaxAge: float | None
    incomingHighWaterMark: int
    outgoingHighWaterMark: int

class WebTransport:
    @classmethod
    def new(self, url: USVString, options: WebTransportOptions | None = {}) -> WebTransport: ...
    def getStats(self) -> Awaitable[WebTransportStats]: ...
    ready: Awaitable[None]
    reliability: WebTransportReliabilityMode
    congestionControl: WebTransportCongestionControl
    closed: Awaitable[WebTransportCloseInfo]
    def close(self, closeInfo: WebTransportCloseInfo | None = {}): ...
    datagrams: WebTransportDatagramDuplexStream
    def createBidirectionalStream(self, options: WebTransportSendStreamOptions | None = {}) -> Awaitable[WebTransportBidirectionalStream]: ...
    incomingBidirectionalStreams: ReadableStream
    def createUnidirectionalStream(self, options: WebTransportSendStreamOptions | None = {}) -> Awaitable[WebTransportSendStream]: ...
    incomingUnidirectionalStreams: ReadableStream

class WebTransportHash(TypedDict):
    algorithm: NotRequired[str]
    value: NotRequired[BufferSource]

class WebTransportOptions(TypedDict):
    allowPooling: NotRequired[bool]
    requireUnreliable: NotRequired[bool]
    serverCertificateHashes: NotRequired[Sequence[WebTransportHash]]
    congestionControl: NotRequired[WebTransportCongestionControl]

class WebTransportCloseInfo(TypedDict):
    closeCode: NotRequired[int]
    reason: NotRequired[USVString]

class WebTransportSendStreamOptions(TypedDict):
    sendOrder: NotRequired[int | None]

class WebTransportStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    bytesSent: NotRequired[int]
    packetsSent: NotRequired[int]
    packetsLost: NotRequired[int]
    numOutgoingStreamsCreated: NotRequired[int]
    numIncomingStreamsCreated: NotRequired[int]
    bytesReceived: NotRequired[int]
    packetsReceived: NotRequired[int]
    smoothedRtt: NotRequired[DOMHighResTimeStamp]
    rttVariation: NotRequired[DOMHighResTimeStamp]
    minRtt: NotRequired[DOMHighResTimeStamp]
    datagrams: NotRequired[WebTransportDatagramStats]

class WebTransportDatagramStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    expiredOutgoing: NotRequired[int]
    droppedIncoming: NotRequired[int]
    lostOutgoing: NotRequired[int]

class WebTransportSendStream(WritableStream):
    def getStats(self) -> Awaitable[WebTransportSendStreamStats]: ...

class WebTransportSendStreamStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    bytesWritten: NotRequired[int]
    bytesSent: NotRequired[int]
    bytesAcknowledged: NotRequired[int]

class WebTransportReceiveStream(ReadableStream):
    def getStats(self) -> Awaitable[WebTransportReceiveStreamStats]: ...

class WebTransportReceiveStreamStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    bytesReceived: NotRequired[int]
    bytesRead: NotRequired[int]

class WebTransportBidirectionalStream:
    readable: WebTransportReceiveStream
    writable: WebTransportSendStream

class WebTransportError(DOMException):
    @classmethod
    def new(self, init: WebTransportErrorInit | None = {}) -> WebTransportError: ...
    source: WebTransportErrorSource
    streamErrorCode: octet | None

class WebTransportErrorInit(TypedDict):
    streamErrorCode: NotRequired[octet]
    message: NotRequired[str]

class USBDeviceFilter(TypedDict):
    vendorId: NotRequired[int]
    productId: NotRequired[int]
    classCode: NotRequired[octet]
    subclassCode: NotRequired[octet]
    protocolCode: NotRequired[octet]
    serialNumber: NotRequired[str]

class USBDeviceRequestOptions(TypedDict):
    filters: Sequence[USBDeviceFilter]

class USB(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    def getDevices(self) -> Awaitable[Sequence[USBDevice]]: ...
    def requestDevice(self, options: USBDeviceRequestOptions) -> Awaitable[USBDevice]: ...

class USBConnectionEventInit(TypedDict, EventInit):
    device: USBDevice

class USBConnectionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: USBConnectionEventInit) -> USBConnectionEvent: ...
    device: USBDevice

class USBInTransferResult:
    @classmethod
    def new(self, status: USBTransferStatus, data: DataView | None = None) -> USBInTransferResult: ...
    data: DataView
    status: USBTransferStatus

class USBOutTransferResult:
    @classmethod
    def new(self, status: USBTransferStatus, bytesWritten: int | None = 0) -> USBOutTransferResult: ...
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousInTransferPacket:
    @classmethod
    def new(self, status: USBTransferStatus, data: DataView | None = None) -> USBIsochronousInTransferPacket: ...
    data: DataView
    status: USBTransferStatus

class USBIsochronousInTransferResult:
    @classmethod
    def new(self, packets: Sequence[USBIsochronousInTransferPacket], data: DataView | None = None) -> USBIsochronousInTransferResult: ...
    data: DataView
    packets: Sequence[USBIsochronousInTransferPacket]

class USBIsochronousOutTransferPacket:
    @classmethod
    def new(self, status: USBTransferStatus, bytesWritten: int | None = 0) -> USBIsochronousOutTransferPacket: ...
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousOutTransferResult:
    @classmethod
    def new(self, packets: Sequence[USBIsochronousOutTransferPacket]) -> USBIsochronousOutTransferResult: ...
    packets: Sequence[USBIsochronousOutTransferPacket]

class USBDevice:
    usbVersionMajor: octet
    usbVersionMinor: octet
    usbVersionSubminor: octet
    deviceClass: octet
    deviceSubclass: octet
    deviceProtocol: octet
    vendorId: int
    productId: int
    deviceVersionMajor: octet
    deviceVersionMinor: octet
    deviceVersionSubminor: octet
    manufacturerName: str | None
    productName: str | None
    serialNumber: str | None
    configuration: USBConfiguration | None
    configurations: Sequence[USBConfiguration]
    opened: bool
    def open(self) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def forget(self) -> Awaitable[None]: ...
    def selectConfiguration(self, configurationValue: octet) -> Awaitable[None]: ...
    def claimInterface(self, interfaceNumber: octet) -> Awaitable[None]: ...
    def releaseInterface(self, interfaceNumber: octet) -> Awaitable[None]: ...
    def selectAlternateInterface(self, interfaceNumber: octet, alternateSetting: octet) -> Awaitable[None]: ...
    def controlTransferIn(self, setup: USBControlTransferParameters, length: int) -> Awaitable[USBInTransferResult]: ...
    def controlTransferOut(self, setup: USBControlTransferParameters, data: BufferSource | None = None) -> Awaitable[USBOutTransferResult]: ...
    def clearHalt(self, direction: USBDirection, endpointNumber: octet) -> Awaitable[None]: ...
    def transferIn(self, endpointNumber: octet, length: int) -> Awaitable[USBInTransferResult]: ...
    def transferOut(self, endpointNumber: octet, data: BufferSource) -> Awaitable[USBOutTransferResult]: ...
    def isochronousTransferIn(self, endpointNumber: octet, packetLengths: Sequence[int]) -> Awaitable[USBIsochronousInTransferResult]: ...
    def isochronousTransferOut(self, endpointNumber: octet, data: BufferSource, packetLengths: Sequence[int]) -> Awaitable[USBIsochronousOutTransferResult]: ...
    def reset(self) -> Awaitable[None]: ...

class USBControlTransferParameters(TypedDict):
    requestType: USBRequestType
    recipient: USBRecipient
    request: octet
    value: int
    index: int

class USBConfiguration:
    @classmethod
    def new(self, device: USBDevice, configurationValue: octet) -> USBConfiguration: ...
    configurationValue: octet
    configurationName: str | None
    interfaces: Sequence[USBInterface]

class USBInterface:
    @classmethod
    def new(self, configuration: USBConfiguration, interfaceNumber: octet) -> USBInterface: ...
    interfaceNumber: octet
    alternate: USBAlternateInterface
    alternates: Sequence[USBAlternateInterface]
    claimed: bool

class USBAlternateInterface:
    @classmethod
    def new(self, deviceInterface: USBInterface, alternateSetting: octet) -> USBAlternateInterface: ...
    alternateSetting: octet
    interfaceClass: octet
    interfaceSubclass: octet
    interfaceProtocol: octet
    interfaceName: str | None
    endpoints: Sequence[USBEndpoint]

class USBEndpoint:
    @classmethod
    def new(self, alternate: USBAlternateInterface, endpointNumber: octet, direction: USBDirection) -> USBEndpoint: ...
    endpointNumber: octet
    direction: USBDirection
    type: USBEndpointType
    packetSize: int

class USBPermissionDescriptor(TypedDict, PermissionDescriptor):
    filters: NotRequired[Sequence[USBDeviceFilter]]

class AllowedUSBDevice(TypedDict):
    vendorId: octet
    productId: octet
    serialNumber: NotRequired[str]

class USBPermissionStorage(TypedDict):
    allowedDevices: NotRequired[Sequence[AllowedUSBDevice]]

class USBPermissionResult(PermissionStatus):
    devices: Sequence[USBDevice]

class VTTCue(TextTrackCue):
    @classmethod
    def new(self, startTime: float, endTime: float, text: str) -> VTTCue: ...
    region: VTTRegion | None
    vertical: DirectionSetting
    snapToLines: bool
    line: LineAndPositionSetting
    lineAlign: LineAlignSetting
    position: LineAndPositionSetting
    positionAlign: PositionAlignSetting
    size: float
    align: AlignSetting
    text: str
    def getCueAsHTML(self) -> DocumentFragment: ...

class VTTRegion:
    @classmethod
    def new(self) -> VTTRegion: ...
    id: str
    width: float
    lines: int
    regionAnchorX: float
    regionAnchorY: float
    viewportAnchorX: float
    viewportAnchorY: float
    scroll: ScrollSetting

class XRDepthStateInit(TypedDict):
    usagePreference: Sequence[XRDepthUsage]
    dataFormatPreference: Sequence[XRDepthDataFormat]

class XRSessionInit(TypedDict, TypedDict, TypedDict):
    depthSensing: NotRequired[XRDepthStateInit]
    domOverlay: NotRequired[XRDOMOverlayInit | None]
    requiredFeatures: NotRequired[Sequence[str]]
    optionalFeatures: NotRequired[Sequence[str]]

class XRDepthInformation:
    width: int
    height: int
    normDepthBufferFromNormView: XRRigidTransform
    rawValueToMeters: float

class XRCPUDepthInformation(XRDepthInformation):
    data: ArrayBuffer
    def getDepthInMeters(self, x: float, y: float) -> float: ...

class XRWebGLDepthInformation(XRDepthInformation):
    texture: WebGLTexture

class XRDOMOverlayInit(TypedDict):
    root: Element

class XRDOMOverlayState(TypedDict):
    type: NotRequired[XRDOMOverlayType]

class XRInputSource:
    gamepad: Gamepad | None
    hand: XRHand | None
    handedness: XRHandedness
    targetRayMode: XRTargetRayMode
    targetRaySpace: XRSpace
    gripSpace: XRSpace | None
    profiles: Sequence[str]

class XRHand:
    size: int
    def get(self, key: XRHandJoint) -> XRJointSpace: ...

class XRJointSpace(XRSpace):
    jointName: XRHandJoint

class XRJointPose(XRPose):
    radius: float

class XRHitTestOptionsInit(TypedDict):
    space: XRSpace
    entityTypes: NotRequired[Sequence[XRHitTestTrackableType]]
    offsetRay: NotRequired[XRRay]

class XRTransientInputHitTestOptionsInit(TypedDict):
    profile: str
    entityTypes: NotRequired[Sequence[XRHitTestTrackableType]]
    offsetRay: NotRequired[XRRay]

class XRHitTestSource:
    def cancel(self): ...

class XRTransientInputHitTestSource:
    def cancel(self): ...

class XRTransientInputHitTestResult:
    inputSource: XRInputSource
    results: Sequence[XRHitTestResult]

class XRRayDirectionInit(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]
    z: NotRequired[float]
    w: NotRequired[float]

class XRRay:
    @overload
    @classmethod
    def new(self, origin: DOMPointInit | None = {}, direction: XRRayDirectionInit | None = {}) -> XRRay: ...
    @overload
    @classmethod
    def new(self, transform: XRRigidTransform) -> XRRay: ...
    origin: DOMPointReadOnly
    direction: DOMPointReadOnly
    matrix: Float32Array

class XRLightProbe(EventTarget):
    probeSpace: XRSpace
    onreflectionchange: EventHandler

class XRLightEstimate:
    sphericalHarmonicsCoefficients: Float32Array
    primaryLightDirection: DOMPointReadOnly
    primaryLightIntensity: DOMPointReadOnly

class XRLightProbeInit(TypedDict):
    reflectionFormat: NotRequired[XRReflectionFormat]

class XRSystem(EventTarget):
    def isSessionSupported(self, mode: XRSessionMode) -> Awaitable[bool]: ...
    def requestSession(self, mode: XRSessionMode, options: XRSessionInit | None = {}) -> Awaitable[XRSession]: ...
    ondevicechange: EventHandler

class XRRenderStateInit(TypedDict):
    depthNear: NotRequired[float]
    depthFar: NotRequired[float]
    inlineVerticalFieldOfView: NotRequired[float]
    baseLayer: NotRequired[XRWebGLLayer | None]
    layers: NotRequired[Sequence[XRLayer]]

class XRRenderState:
    depthNear: float
    depthFar: float
    inlineVerticalFieldOfView: float | None
    baseLayer: XRWebGLLayer | None
    layers: Sequence[XRLayer]

class XRSpace(EventTarget): ...

class XRReferenceSpace(XRSpace):
    def getOffsetReferenceSpace(self, originOffset: XRRigidTransform) -> XRReferenceSpace: ...
    onreset: EventHandler

class XRBoundedReferenceSpace(XRReferenceSpace):
    boundsGeometry: Sequence[DOMPointReadOnly]

class XRViewport:
    x: int
    y: int
    width: int
    height: int

class XRRigidTransform:
    @classmethod
    def new(self, position: DOMPointInit | None = {}, orientation: DOMPointInit | None = {}) -> XRRigidTransform: ...
    position: DOMPointReadOnly
    orientation: DOMPointReadOnly
    matrix: Float32Array
    inverse: XRRigidTransform

class XRPose:
    transform: XRRigidTransform
    linearVelocity: DOMPointReadOnly | None
    angularVelocity: DOMPointReadOnly | None
    emulatedPosition: bool

class XRViewerPose(XRPose):
    views: Sequence[XRView]

class XRInputSourceArray:
    length: int

class XRLayer(EventTarget): ...

class XRWebGLLayerInit(TypedDict):
    antialias: NotRequired[bool]
    depth: NotRequired[bool]
    stencil: NotRequired[bool]
    alpha: NotRequired[bool]
    ignoreDepthValues: NotRequired[bool]
    framebufferScaleFactor: NotRequired[float]

class XRWebGLLayer(XRLayer):
    @classmethod
    def new(self, session: XRSession, context: XRWebGLRenderingContext, layerInit: XRWebGLLayerInit | None = {}) -> XRWebGLLayer: ...
    antialias: bool
    ignoreDepthValues: bool
    fixedFoveation: float | None
    framebuffer: WebGLFramebuffer | None
    framebufferWidth: int
    framebufferHeight: int
    def getViewport(self, view: XRView) -> XRViewport | None: ...

class XRSessionEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: XRSessionEventInit) -> XRSessionEvent: ...
    session: XRSession

class XRSessionEventInit(TypedDict, EventInit):
    session: XRSession

class XRInputSourceEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: XRInputSourceEventInit) -> XRInputSourceEvent: ...
    frame: XRFrame
    inputSource: XRInputSource

class XRInputSourceEventInit(TypedDict, EventInit):
    frame: XRFrame
    inputSource: XRInputSource

class XRInputSourcesChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: XRInputSourcesChangeEventInit) -> XRInputSourcesChangeEvent: ...
    session: XRSession
    added: Sequence[XRInputSource]
    removed: Sequence[XRInputSource]

class XRInputSourcesChangeEventInit(TypedDict, EventInit):
    session: XRSession
    added: Sequence[XRInputSource]
    removed: Sequence[XRInputSource]

class XRReferenceSpaceEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: XRReferenceSpaceEventInit) -> XRReferenceSpaceEvent: ...
    referenceSpace: XRReferenceSpace
    transform: XRRigidTransform | None

class XRReferenceSpaceEventInit(TypedDict, EventInit):
    referenceSpace: XRReferenceSpace
    transform: NotRequired[XRRigidTransform | None]

class XRSessionSupportedPermissionDescriptor(TypedDict, PermissionDescriptor):
    mode: NotRequired[XRSessionMode]

class XRPermissionDescriptor(TypedDict, PermissionDescriptor):
    mode: NotRequired[XRSessionMode]
    requiredFeatures: NotRequired[Sequence[str]]
    optionalFeatures: NotRequired[Sequence[str]]

class XRPermissionStatus(PermissionStatus):
    granted: Sequence[str]

class XRCompositionLayer(XRLayer):
    layout: XRLayerLayout
    blendTextureSourceAlpha: bool
    chromaticAberrationCorrection: bool | None
    forceMonoPresentation: bool
    opacity: float
    mipLevels: int
    needsRedraw: bool
    def destroy(self): ...

class XRProjectionLayer(XRCompositionLayer):
    textureWidth: int
    textureHeight: int
    textureArrayLength: int
    ignoreDepthValues: bool
    fixedFoveation: float | None
    deltaPose: XRRigidTransform | None

class XRQuadLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    width: float
    height: float
    onredraw: EventHandler

class XRCylinderLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    radius: float
    centralAngle: float
    aspectRatio: float
    onredraw: EventHandler

class XREquirectLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    radius: float
    centralHorizontalAngle: float
    upperVerticalAngle: float
    lowerVerticalAngle: float
    onredraw: EventHandler

class XRCubeLayer(XRCompositionLayer):
    space: XRSpace
    orientation: DOMPointReadOnly
    onredraw: EventHandler

class XRSubImage:
    viewport: XRViewport

class XRWebGLSubImage(XRSubImage):
    colorTexture: WebGLTexture
    depthStencilTexture: WebGLTexture | None
    motionVectorTexture: WebGLTexture | None
    imageIndex: int | None
    colorTextureWidth: int
    colorTextureHeight: int
    depthStencilTextureWidth: int | None
    depthStencilTextureHeight: int | None
    motionVectorTextureWidth: int | None
    motionVectorTextureHeight: int | None

class XRProjectionLayerInit(TypedDict):
    textureType: NotRequired[XRTextureType]
    colorFormat: NotRequired[GLenum]
    depthFormat: NotRequired[GLenum]
    scaleFactor: NotRequired[float]

class XRLayerInit(TypedDict):
    space: XRSpace
    colorFormat: NotRequired[GLenum]
    depthFormat: NotRequired[GLenum | None]
    mipLevels: NotRequired[int]
    viewPixelWidth: int
    viewPixelHeight: int
    layout: NotRequired[XRLayerLayout]
    isStatic: NotRequired[bool]

class XRQuadLayerInit(TypedDict, XRLayerInit):
    textureType: NotRequired[XRTextureType]
    transform: NotRequired[XRRigidTransform | None]
    width: NotRequired[float]
    height: NotRequired[float]

class XRCylinderLayerInit(TypedDict, XRLayerInit):
    textureType: NotRequired[XRTextureType]
    transform: NotRequired[XRRigidTransform | None]
    radius: NotRequired[float]
    centralAngle: NotRequired[float]
    aspectRatio: NotRequired[float]

class XREquirectLayerInit(TypedDict, XRLayerInit):
    textureType: NotRequired[XRTextureType]
    transform: NotRequired[XRRigidTransform | None]
    radius: NotRequired[float]
    centralHorizontalAngle: NotRequired[float]
    upperVerticalAngle: NotRequired[float]
    lowerVerticalAngle: NotRequired[float]

class XRCubeLayerInit(TypedDict, XRLayerInit):
    orientation: NotRequired[DOMPointReadOnly | None]

class XRMediaLayerInit(TypedDict):
    space: XRSpace
    layout: NotRequired[XRLayerLayout]
    invertStereo: NotRequired[bool]

class XRMediaQuadLayerInit(TypedDict, XRMediaLayerInit):
    transform: NotRequired[XRRigidTransform | None]
    width: NotRequired[float | None]
    height: NotRequired[float | None]

class XRMediaCylinderLayerInit(TypedDict, XRMediaLayerInit):
    transform: NotRequired[XRRigidTransform | None]
    radius: NotRequired[float]
    centralAngle: NotRequired[float]
    aspectRatio: NotRequired[float | None]

class XRMediaEquirectLayerInit(TypedDict, XRMediaLayerInit):
    transform: NotRequired[XRRigidTransform | None]
    radius: NotRequired[float]
    centralHorizontalAngle: NotRequired[float]
    upperVerticalAngle: NotRequired[float]
    lowerVerticalAngle: NotRequired[float]

class XRMediaBinding:
    @classmethod
    def new(self, session: XRSession) -> XRMediaBinding: ...
    def createQuadLayer(self, video: HTMLVideoElement, init: XRMediaQuadLayerInit | None = {}) -> XRQuadLayer: ...
    def createCylinderLayer(self, video: HTMLVideoElement, init: XRMediaCylinderLayerInit | None = {}) -> XRCylinderLayer: ...
    def createEquirectLayer(self, video: HTMLVideoElement, init: XRMediaEquirectLayerInit | None = {}) -> XREquirectLayer: ...

class XRLayerEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: XRLayerEventInit) -> XRLayerEvent: ...
    layer: XRLayer

class XRLayerEventInit(TypedDict, EventInit):
    layer: XRLayer

class WindowControlsOverlay(EventTarget):
    visible: bool
    def getTitlebarAreaRect(self) -> DOMRect: ...
    ongeometrychange: EventHandler

class WindowControlsOverlayGeometryChangeEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: WindowControlsOverlayGeometryChangeEventInit) -> WindowControlsOverlayGeometryChangeEvent: ...
    titlebarAreaRect: DOMRect
    visible: bool

class WindowControlsOverlayGeometryChangeEventInit(TypedDict, EventInit):
    titlebarAreaRect: DOMRect
    visible: NotRequired[bool]

class ScreenDetails(EventTarget):
    screens: Sequence[ScreenDetailed]
    currentScreen: ScreenDetailed
    onscreenschange: EventHandler
    oncurrentscreenchange: EventHandler

class ScreenDetailed(Screen):
    availLeft: int
    availTop: int
    left: int
    top: int
    isPrimary: bool
    isInternal: bool
    devicePixelRatio: float
    label: str

class XMLHttpRequestEventTarget(EventTarget):
    onloadstart: EventHandler
    onprogress: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onload: EventHandler
    ontimeout: EventHandler
    onloadend: EventHandler

class XMLHttpRequestUpload(XMLHttpRequestEventTarget): ...

class XMLHttpRequest(XMLHttpRequestEventTarget):
    @classmethod
    def new(self) -> XMLHttpRequest: ...
    onreadystatechange: EventHandler
    UNSENT = 0
    OPENED = 1
    HEADERS_RECEIVED = 2
    LOADING = 3
    DONE = 4
    readyState: int
    @overload
    def open(self, method: ByteString, url: USVString): ...
    @overload
    def open(self, method: ByteString, url: USVString, async_: bool, username: USVString | None = None, password: USVString | None = None): ...
    def setRequestHeader(self, name: ByteString, value: ByteString): ...
    timeout: int
    withCredentials: bool
    upload: XMLHttpRequestUpload
    def send(self, body: Document | XMLHttpRequestBodyInit | None = None): ...
    def abort(self): ...
    responseURL: USVString
    status: int
    statusText: ByteString
    def getResponseHeader(self, name: ByteString) -> ByteString | None: ...
    def getAllResponseHeaders(self) -> ByteString: ...
    def overrideMimeType(self, mime: str): ...
    responseType: XMLHttpRequestResponseType
    response: Any
    responseText: USVString
    responseXML: Document | None

class FormData:
    @classmethod
    def new(self, form: HTMLFormElement | None = None) -> FormData: ...
    @overload
    def append(self, name: USVString, value: USVString): ...
    @overload
    def append(self, name: USVString, blobValue: Blob, filename: USVString | None = None): ...
    def delete(self, name: USVString): ...
    def get(self, name: USVString) -> FormDataEntryValue | None: ...
    def getAll(self, name: USVString) -> Sequence[FormDataEntryValue]: ...
    def has(self, name: USVString) -> bool: ...
    @overload
    def set(self, name: USVString, value: USVString): ...
    @overload
    def set(self, name: USVString, blobValue: Blob, filename: USVString | None = None): ...

class ProgressEvent(Event):
    @classmethod
    def new(self, type: str, eventInitDict: ProgressEventInit | None = {}) -> ProgressEvent: ...
    lengthComputable: bool
    loaded: int
    total: int

class ProgressEventInit(TypedDict, EventInit):
    lengthComputable: NotRequired[bool]
    loaded: NotRequired[int]
    total: NotRequired[int]



document: Document
window: Window
navigator: Navigator
console: ConsoleNamespace

