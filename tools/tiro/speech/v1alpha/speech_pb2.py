# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tiro/speech/v1alpha/speech.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tiro/speech/v1alpha/speech.proto\x12\x13tiro.speech.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/rpc/status.proto\"\x8a\x01\n\x10RecognizeRequest\x12;\n\x06\x63onfig\x18\x01 \x01(\x0b\x32&.tiro.speech.v1alpha.RecognitionConfigB\x03\xe0\x41\x02\x12\x39\n\x05\x61udio\x18\x02 \x01(\x0b\x32%.tiro.speech.v1alpha.RecognitionAudioB\x03\xe0\x41\x02\"\x96\x01\n\x19StreamingRecognizeRequest\x12K\n\x10streaming_config\x18\x01 \x01(\x0b\x32/.tiro.speech.v1alpha.StreamingRecognitionConfigH\x00\x12\x17\n\raudio_content\x18\x02 \x01(\x0cH\x00\x42\x13\n\x11streaming_request\"\x8c\x01\n\x1aStreamingRecognitionConfig\x12;\n\x06\x63onfig\x18\x01 \x01(\x0b\x32&.tiro.speech.v1alpha.RecognitionConfigB\x03\xe0\x41\x02\x12\x18\n\x10single_utterance\x18\x02 \x01(\x08\x12\x17\n\x0finterim_results\x18\x03 \x01(\x08\"\xd3\x03\n\x11RecognitionConfig\x12\x46\n\x08\x65ncoding\x18\x01 \x01(\x0e\x32\x34.tiro.speech.v1alpha.RecognitionConfig.AudioEncoding\x12\x19\n\x11sample_rate_hertz\x18\x02 \x01(\x05\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0\x41\x02\x12\x18\n\x10max_alternatives\x18\x04 \x01(\x05\x12 \n\x18\x65nable_word_time_offsets\x18\x08 \x01(\x08\x12:\n\x08metadata\x18\t \x01(\x0b\x32(.tiro.speech.v1alpha.RecognitionMetadata\x12$\n\x1c\x65nable_automatic_punctuation\x18\x0b \x01(\x08\x12I\n\x12\x64iarization_config\x18\x13 \x01(\x0b\x32-.tiro.speech.v1alpha.SpeakerDiarizationConfig\"J\n\rAudioEncoding\x12\x18\n\x14\x45NCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x08\n\x04\x46LAC\x10\x02\x12\x07\n\x03MP3\x10\x08J\x04\x08\x07\x10\x08J\x04\x08\x0c\x10\r\"\x87\x01\n\x18SpeakerDiarizationConfig\x12\"\n\x1a\x65nable_speaker_diarization\x18\x01 \x01(\x08\x12\x19\n\x11min_speaker_count\x18\x02 \x01(\x05\x12\x19\n\x11max_speaker_count\x18\x03 \x01(\x05J\x04\x08\x05\x10\x06R\x0bspeaker_tag\"\x94\x08\n\x13RecognitionMetadata\x12R\n\x10interaction_type\x18\x01 \x01(\x0e\x32\x38.tiro.speech.v1alpha.RecognitionMetadata.InteractionType\x12$\n\x1cindustry_naics_code_of_audio\x18\x03 \x01(\r\x12X\n\x13microphone_distance\x18\x04 \x01(\x0e\x32;.tiro.speech.v1alpha.RecognitionMetadata.MicrophoneDistance\x12W\n\x13original_media_type\x18\x05 \x01(\x0e\x32:.tiro.speech.v1alpha.RecognitionMetadata.OriginalMediaType\x12[\n\x15recording_device_type\x18\x06 \x01(\x0e\x32<.tiro.speech.v1alpha.RecognitionMetadata.RecordingDeviceType\x12\x1d\n\x15recording_device_name\x18\x07 \x01(\t\x12\x1a\n\x12original_mime_type\x18\x08 \x01(\t\x12\x13\n\x0b\x61udio_topic\x18\n \x01(\t\"\xc5\x01\n\x0fInteractionType\x12 \n\x1cINTERACTION_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nDISCUSSION\x10\x01\x12\x10\n\x0cPRESENTATION\x10\x02\x12\x0e\n\nPHONE_CALL\x10\x03\x12\r\n\tVOICEMAIL\x10\x04\x12\x1b\n\x17PROFESSIONALLY_PRODUCED\x10\x05\x12\x10\n\x0cVOICE_SEARCH\x10\x06\x12\x11\n\rVOICE_COMMAND\x10\x07\x12\r\n\tDICTATION\x10\x08\"d\n\x12MicrophoneDistance\x12#\n\x1fMICROPHONE_DISTANCE_UNSPECIFIED\x10\x00\x12\r\n\tNEARFIELD\x10\x01\x12\x0c\n\x08MIDFIELD\x10\x02\x12\x0c\n\x08\x46\x41RFIELD\x10\x03\"N\n\x11OriginalMediaType\x12#\n\x1fORIGINAL_MEDIA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x41UDIO\x10\x01\x12\t\n\x05VIDEO\x10\x02\"\xa4\x01\n\x13RecordingDeviceType\x12%\n!RECORDING_DEVICE_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nSMARTPHONE\x10\x01\x12\x06\n\x02PC\x10\x02\x12\x0e\n\nPHONE_LINE\x10\x03\x12\x0b\n\x07VEHICLE\x10\x04\x12\x18\n\x14OTHER_OUTDOOR_DEVICE\x10\x05\x12\x17\n\x13OTHER_INDOOR_DEVICE\x10\x06\"D\n\x10RecognitionAudio\x12\x11\n\x07\x63ontent\x18\x01 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x02 \x01(\tH\x00\x42\x0e\n\x0c\x61udio_source\"R\n\x11RecognizeResponse\x12=\n\x07results\x18\x02 \x03(\x0b\x32,.tiro.speech.v1alpha.SpeechRecognitionResult\"\xab\x02\n\x1aStreamingRecognizeResponse\x12!\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12@\n\x07results\x18\x02 \x03(\x0b\x32/.tiro.speech.v1alpha.StreamingRecognitionResult\x12Z\n\x11speech_event_type\x18\x04 \x01(\x0e\x32?.tiro.speech.v1alpha.StreamingRecognizeResponse.SpeechEventType\"L\n\x0fSpeechEventType\x12\x1c\n\x18SPEECH_EVENT_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x45ND_OF_SINGLE_UTTERANCE\x10\x01\"\xc9\x01\n\x1aStreamingRecognitionResult\x12G\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x31.tiro.speech.v1alpha.SpeechRecognitionAlternative\x12\x10\n\x08is_final\x18\x02 \x01(\x08\x12\x11\n\tstability\x18\x03 \x01(\x02J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07R\x0fresult_end_timeR\x0b\x63hannel_tagR\rlanguage_code\"n\n\x17SpeechRecognitionResult\x12G\n\x0c\x61lternatives\x18\x01 \x03(\x0b\x32\x31.tiro.speech.v1alpha.SpeechRecognitionAlternativeJ\x04\x08\x02\x10\x03J\x04\x08\x05\x10\x06\"t\n\x1cSpeechRecognitionAlternative\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12,\n\x05words\x18\x03 \x03(\x0b\x32\x1d.tiro.speech.v1alpha.WordInfo\"\xa2\x01\n\x08WordInfo\x12-\n\nstart_time\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12+\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x0c\n\x04word\x18\x03 \x01(\t\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x18\n\x0bspeaker_tag\x18\x05 \x01(\x05\x42\x03\xe0\x41\x03\x32\xaa\x02\n\x06Speech\x12\x8f\x01\n\tRecognize\x12%.tiro.speech.v1alpha.RecognizeRequest\x1a&.tiro.speech.v1alpha.RecognizeResponse\"3\x82\xd3\xe4\x93\x02\x1e\"\x19/v1alpha/speech:recognize:\x01*\xda\x41\x0c\x63onfig,audio\x12{\n\x12StreamingRecognize\x12..tiro.speech.v1alpha.StreamingRecognizeRequest\x1a/.tiro.speech.v1alpha.StreamingRecognizeResponse\"\x00(\x01\x30\x01\x1a\x11\xca\x41\x0espeech.tiro.isBn\n\x16is.tiro.speech.v1alphaB\x0bSpeechProtoP\x01Z=gitlab.com/tiro-is/tiro-apis-gogen/tiro/speech/v1alpha;speech\xf8\x01\x01\xa2\x02\x02TSb\x06proto3')



_RECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['RecognizeRequest']
_STREAMINGRECOGNIZEREQUEST = DESCRIPTOR.message_types_by_name['StreamingRecognizeRequest']
_STREAMINGRECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['StreamingRecognitionConfig']
_RECOGNITIONCONFIG = DESCRIPTOR.message_types_by_name['RecognitionConfig']
_SPEAKERDIARIZATIONCONFIG = DESCRIPTOR.message_types_by_name['SpeakerDiarizationConfig']
_RECOGNITIONMETADATA = DESCRIPTOR.message_types_by_name['RecognitionMetadata']
_RECOGNITIONAUDIO = DESCRIPTOR.message_types_by_name['RecognitionAudio']
_RECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['RecognizeResponse']
_STREAMINGRECOGNIZERESPONSE = DESCRIPTOR.message_types_by_name['StreamingRecognizeResponse']
_STREAMINGRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['StreamingRecognitionResult']
_SPEECHRECOGNITIONRESULT = DESCRIPTOR.message_types_by_name['SpeechRecognitionResult']
_SPEECHRECOGNITIONALTERNATIVE = DESCRIPTOR.message_types_by_name['SpeechRecognitionAlternative']
_WORDINFO = DESCRIPTOR.message_types_by_name['WordInfo']
_RECOGNITIONCONFIG_AUDIOENCODING = _RECOGNITIONCONFIG.enum_types_by_name['AudioEncoding']
_RECOGNITIONMETADATA_INTERACTIONTYPE = _RECOGNITIONMETADATA.enum_types_by_name['InteractionType']
_RECOGNITIONMETADATA_MICROPHONEDISTANCE = _RECOGNITIONMETADATA.enum_types_by_name['MicrophoneDistance']
_RECOGNITIONMETADATA_ORIGINALMEDIATYPE = _RECOGNITIONMETADATA.enum_types_by_name['OriginalMediaType']
_RECOGNITIONMETADATA_RECORDINGDEVICETYPE = _RECOGNITIONMETADATA.enum_types_by_name['RecordingDeviceType']
_STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE = _STREAMINGRECOGNIZERESPONSE.enum_types_by_name['SpeechEventType']
RecognizeRequest = _reflection.GeneratedProtocolMessageType('RecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZEREQUEST,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.RecognizeRequest)
  })
_sym_db.RegisterMessage(RecognizeRequest)

StreamingRecognizeRequest = _reflection.GeneratedProtocolMessageType('StreamingRecognizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZEREQUEST,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.StreamingRecognizeRequest)
  })
_sym_db.RegisterMessage(StreamingRecognizeRequest)

StreamingRecognitionConfig = _reflection.GeneratedProtocolMessageType('StreamingRecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONCONFIG,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.StreamingRecognitionConfig)
  })
_sym_db.RegisterMessage(StreamingRecognitionConfig)

RecognitionConfig = _reflection.GeneratedProtocolMessageType('RecognitionConfig', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONCONFIG,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.RecognitionConfig)
  })
_sym_db.RegisterMessage(RecognitionConfig)

SpeakerDiarizationConfig = _reflection.GeneratedProtocolMessageType('SpeakerDiarizationConfig', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKERDIARIZATIONCONFIG,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.SpeakerDiarizationConfig)
  })
_sym_db.RegisterMessage(SpeakerDiarizationConfig)

RecognitionMetadata = _reflection.GeneratedProtocolMessageType('RecognitionMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONMETADATA,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.RecognitionMetadata)
  })
_sym_db.RegisterMessage(RecognitionMetadata)

RecognitionAudio = _reflection.GeneratedProtocolMessageType('RecognitionAudio', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNITIONAUDIO,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.RecognitionAudio)
  })
_sym_db.RegisterMessage(RecognitionAudio)

RecognizeResponse = _reflection.GeneratedProtocolMessageType('RecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOGNIZERESPONSE,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.RecognizeResponse)
  })
_sym_db.RegisterMessage(RecognizeResponse)

StreamingRecognizeResponse = _reflection.GeneratedProtocolMessageType('StreamingRecognizeResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNIZERESPONSE,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.StreamingRecognizeResponse)
  })
_sym_db.RegisterMessage(StreamingRecognizeResponse)

StreamingRecognitionResult = _reflection.GeneratedProtocolMessageType('StreamingRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINGRECOGNITIONRESULT,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.StreamingRecognitionResult)
  })
_sym_db.RegisterMessage(StreamingRecognitionResult)

SpeechRecognitionResult = _reflection.GeneratedProtocolMessageType('SpeechRecognitionResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONRESULT,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.SpeechRecognitionResult)
  })
_sym_db.RegisterMessage(SpeechRecognitionResult)

SpeechRecognitionAlternative = _reflection.GeneratedProtocolMessageType('SpeechRecognitionAlternative', (_message.Message,), {
  'DESCRIPTOR' : _SPEECHRECOGNITIONALTERNATIVE,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.SpeechRecognitionAlternative)
  })
_sym_db.RegisterMessage(SpeechRecognitionAlternative)

WordInfo = _reflection.GeneratedProtocolMessageType('WordInfo', (_message.Message,), {
  'DESCRIPTOR' : _WORDINFO,
  '__module__' : 'tiro.speech.v1alpha.speech_pb2'
  # @@protoc_insertion_point(class_scope:tiro.speech.v1alpha.WordInfo)
  })
_sym_db.RegisterMessage(WordInfo)

_SPEECH = DESCRIPTOR.services_by_name['Speech']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026is.tiro.speech.v1alphaB\013SpeechProtoP\001Z=gitlab.com/tiro-is/tiro-apis-gogen/tiro/speech/v1alpha;speech\370\001\001\242\002\002TS'
  _RECOGNIZEREQUEST.fields_by_name['config']._options = None
  _RECOGNIZEREQUEST.fields_by_name['config']._serialized_options = b'\340A\002'
  _RECOGNIZEREQUEST.fields_by_name['audio']._options = None
  _RECOGNIZEREQUEST.fields_by_name['audio']._serialized_options = b'\340A\002'
  _STREAMINGRECOGNITIONCONFIG.fields_by_name['config']._options = None
  _STREAMINGRECOGNITIONCONFIG.fields_by_name['config']._serialized_options = b'\340A\002'
  _RECOGNITIONCONFIG.fields_by_name['language_code']._options = None
  _RECOGNITIONCONFIG.fields_by_name['language_code']._serialized_options = b'\340A\002'
  _WORDINFO.fields_by_name['speaker_tag']._options = None
  _WORDINFO.fields_by_name['speaker_tag']._serialized_options = b'\340A\003'
  _SPEECH._options = None
  _SPEECH._serialized_options = b'\312A\016speech.tiro.is'
  _SPEECH.methods_by_name['Recognize']._options = None
  _SPEECH.methods_by_name['Recognize']._serialized_options = b'\202\323\344\223\002\036\"\031/v1alpha/speech:recognize:\001*\332A\014config,audio'
  _RECOGNIZEREQUEST._serialized_start=203
  _RECOGNIZEREQUEST._serialized_end=341
  _STREAMINGRECOGNIZEREQUEST._serialized_start=344
  _STREAMINGRECOGNIZEREQUEST._serialized_end=494
  _STREAMINGRECOGNITIONCONFIG._serialized_start=497
  _STREAMINGRECOGNITIONCONFIG._serialized_end=637
  _RECOGNITIONCONFIG._serialized_start=640
  _RECOGNITIONCONFIG._serialized_end=1107
  _RECOGNITIONCONFIG_AUDIOENCODING._serialized_start=1021
  _RECOGNITIONCONFIG_AUDIOENCODING._serialized_end=1095
  _SPEAKERDIARIZATIONCONFIG._serialized_start=1110
  _SPEAKERDIARIZATIONCONFIG._serialized_end=1245
  _RECOGNITIONMETADATA._serialized_start=1248
  _RECOGNITIONMETADATA._serialized_end=2292
  _RECOGNITIONMETADATA_INTERACTIONTYPE._serialized_start=1746
  _RECOGNITIONMETADATA_INTERACTIONTYPE._serialized_end=1943
  _RECOGNITIONMETADATA_MICROPHONEDISTANCE._serialized_start=1945
  _RECOGNITIONMETADATA_MICROPHONEDISTANCE._serialized_end=2045
  _RECOGNITIONMETADATA_ORIGINALMEDIATYPE._serialized_start=2047
  _RECOGNITIONMETADATA_ORIGINALMEDIATYPE._serialized_end=2125
  _RECOGNITIONMETADATA_RECORDINGDEVICETYPE._serialized_start=2128
  _RECOGNITIONMETADATA_RECORDINGDEVICETYPE._serialized_end=2292
  _RECOGNITIONAUDIO._serialized_start=2294
  _RECOGNITIONAUDIO._serialized_end=2362
  _RECOGNIZERESPONSE._serialized_start=2364
  _RECOGNIZERESPONSE._serialized_end=2446
  _STREAMINGRECOGNIZERESPONSE._serialized_start=2449
  _STREAMINGRECOGNIZERESPONSE._serialized_end=2748
  _STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE._serialized_start=2672
  _STREAMINGRECOGNIZERESPONSE_SPEECHEVENTTYPE._serialized_end=2748
  _STREAMINGRECOGNITIONRESULT._serialized_start=2751
  _STREAMINGRECOGNITIONRESULT._serialized_end=2952
  _SPEECHRECOGNITIONRESULT._serialized_start=2954
  _SPEECHRECOGNITIONRESULT._serialized_end=3064
  _SPEECHRECOGNITIONALTERNATIVE._serialized_start=3066
  _SPEECHRECOGNITIONALTERNATIVE._serialized_end=3182
  _WORDINFO._serialized_start=3185
  _WORDINFO._serialized_end=3347
  _SPEECH._serialized_start=3350
  _SPEECH._serialized_end=3648
# @@protoc_insertion_point(module_scope)
