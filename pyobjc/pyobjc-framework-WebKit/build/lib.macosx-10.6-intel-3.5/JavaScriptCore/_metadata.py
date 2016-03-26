# This file is generated by objective.metadata
#
# Last update: Tue Sep 22 21:30:25 2015

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$JSPropertyDescriptorConfigurableKey$JSPropertyDescriptorEnumerableKey$JSPropertyDescriptorGetKey$JSPropertyDescriptorSetKey$JSPropertyDescriptorValueKey$JSPropertyDescriptorWritableKey$'''
enums = '''$WEBKIT_VERSION_1_0@256$WEBKIT_VERSION_1_1@272$WEBKIT_VERSION_1_2@288$WEBKIT_VERSION_1_3@304$WEBKIT_VERSION_2_0@512$WEBKIT_VERSION_3_0@768$WEBKIT_VERSION_3_1@784$WEBKIT_VERSION_4_0@1024$WEBKIT_VERSION_LATEST@39321$kJSClassAttributeNoAutomaticPrototype@2$kJSClassAttributeNone@0$kJSPropertyAttributeDontDelete@8$kJSPropertyAttributeDontEnum@4$kJSPropertyAttributeNone@0$kJSPropertyAttributeReadOnly@2$kJSTypeBoolean@2$kJSTypeNull@1$kJSTypeNumber@3$kJSTypeObject@5$kJSTypeString@4$kJSTypeUndefined@0$'''
misc.update({})
functions={'JSValueMakeNumber': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}d',), 'JSClassRetain': (b'^{OpaqueJSClass=}^{OpaqueJSClass=}',), 'JSValueCreateJSONString': (b'^{OpaqueJSString=}^{OpaqueJSContext=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSStringCreateWithCharacters': (sel32or64(b'^{OpaqueJSString=}^TL', b'^{OpaqueJSString=}^TQ'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}}}), 'JSObjectMakeFunctionWithCallback': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}^?', '', {'arguments': {2: {'callable': {'retval': {'type': b'^{OpaqueJSValue=}'}, 'arguments': {0: {'type': b'^{OpaqueJSContext=}'}, 1: {'type': b'^{OpaqueJSValue=}'}, 2: {'type': b'^{OpaqueJSValue=}'}, 3: {'type': b'L'}, 4: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'n', 'c_array_length_in_arg': 3}, 5: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'o'}}}}}}), 'JSValueToBoolean': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsObject': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameArrayRetain': (b'^{OpaqueJSPropertyNameArray=}^{OpaqueJSPropertyNameArray=}',), 'JSGlobalContextCopyName': (b'^{OpaqueJSString=}^{OpaqueJSContext=}', '', {'retval': {'already_cfretained': True}}), 'JSStringGetUTF8CString': (sel32or64(b'L^{OpaqueJSString=}^tL', b'Q^{OpaqueJSString=}^tQ'), '', {'arguments': {1: {'c_array_length_in_result': True, 'type_modifier': 'o', 'c_array_length_in_arg': 2}}}), 'JSStringCreateWithCFString': (b'^{OpaqueJSString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectCopyPropertyNames': (b'^{OpaqueJSPropertyNameArray=}^{OpaqueJSContext=}^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSContextGetGlobalObject': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSGlobalContextCreate': (b'^{OpaqueJSContext=}^{OpaqueJSClass=}', '', {'retval': {'already_cfretained': True}}), 'JSStringCopyCFString': (b'^{__CFString=}^{__CFAllocator=}^{OpaqueJSString=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectGetPrivate': (b'^v^{OpaqueJSValue=}',), 'JSObjectSetProperty': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'arguments': {5: {'type_modifier': 'o'}}}), 'JSValueIsEqual': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSObjectIsFunction': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsBoolean': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsUndefined': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueProtect': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsObjectOfClass': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSClass=}',), 'JSObjectGetPrototype': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSStringCreateWithUTF8CString': (b'^{OpaqueJSString=}^t', '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'c_array_delimited_by_null': True, 'type_modifier': 'n'}}}), 'JSObjectMakeArray': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSValueIsArray': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameArrayGetNameAtIndex': (sel32or64(b'^{OpaqueJSString=}^{OpaqueJSPropertyNameArray=}L', b'^{OpaqueJSString=}^{OpaqueJSPropertyNameArray=}Q'),), 'JSValueMakeNull': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSValueIsString': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSGlobalContextSetName': (b'v^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSStringGetMaximumUTF8CStringSize': (sel32or64(b'L^{OpaqueJSString=}', b'Q^{OpaqueJSString=}'),), 'JSObjectMakeError': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSValueMakeBoolean': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}B',), 'JSGlobalContextRelease': (b'v^{OpaqueJSContext=}',), 'JSObjectMakeRegExp': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSObjectSetPropertyAtIndex': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}I^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {4: {'type_modifier': 'o'}}}), 'JSContextGetGroup': (b'^{OpaqueJSContextGroup=}^{OpaqueJSContext=}',), 'JSContextGroupCreate': (b'^{OpaqueJSContextGroup=}', '', {'retval': {'already_cfretained': True}, 'variadic': True}), 'JSStringIsEqualToUTF8CString': (b'B^{OpaqueJSString=}^t', '', {'arguments': {1: {'c_array_delimited_by_null': True, 'type_modifier': 'n'}}}), 'JSValueIsInstanceOfConstructor': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSValueIsNull': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSStringIsEqual': (b'B^{OpaqueJSString=}^{OpaqueJSString=}',), 'JSObjectCallAsConstructor': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {3: {'c_array_length_in_arg': 2, 'type_modifier': 'n'}, 4: {'type_modifier': 'o'}}}), 'JSStringRetain': (b'^{OpaqueJSString=}^{OpaqueJSString=}',), 'JSObjectDeleteProperty': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSObjectMakeConstructor': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSClass=}^?', '', {'arguments': {2: {'callable': {'retval': {'type': b'^{OpaqueJSValue=}'}, 'arguments': {0: {'type': b'^{OpaqueJSContext=}'}, 1: {'type': b'^{OpaqueJSValue=}'}, 2: {'type': b'L'}, 3: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'n', 'c_array_length_in_arg': 2}, 4: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'o'}}}}}}), 'JSValueMakeString': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSObjectSetPrivate': (b'B^{OpaqueJSValue=}^v',), 'JSObjectMakeFunction': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}I^^{OpaqueJSString=}^{OpaqueJSString=}^{OpaqueJSString=}i^^{OpaqueJSValue=}', '', {'arguments': {3: {'c_array_length_in_arg': 2, 'type_modifier': 'n'}, 7: {'type_modifier': 'o'}}}), 'JSValueToStringCopy': (b'^{OpaqueJSString=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSValueMakeFromJSONString': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSValueIsNumber': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSEvaluateScript': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}^{OpaqueJSValue=}^{OpaqueJSString=}i^^{OpaqueJSValue=}', '', {'arguments': {5: {'type_modifier': 'o'}}}), 'JSObjectGetPropertyAtIndex': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSContextGetGlobalContext': (b'^{OpaqueJSContext=}^{OpaqueJSContext=}',), 'JSValueIsDate': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueToNumber': (b'd^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSObjectGetProperty': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSPropertyNameAccumulatorAddName': (b'v^{OpaqueJSPropertyNameAccumulator=}^{OpaqueJSString=}',), 'JSObjectSetPrototype': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}',), 'JSContextGroupRelease': (b'v^{OpaqueJSContextGroup=}',), 'JSObjectHasProperty': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}',), 'JSValueIsStrictEqual': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}',), 'JSObjectMake': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSClass=}^v',), 'JSValueMakeUndefined': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSCheckScriptSyntax': (b'B^{OpaqueJSContext=}^{OpaqueJSString=}^{OpaqueJSString=}i^^{OpaqueJSValue=}', '', {'arguments': {4: {'type_modifier': 'o'}}}), 'JSGlobalContextCreateInGroup': (b'^{OpaqueJSContext=}^{OpaqueJSContextGroup=}^{OpaqueJSClass=}', '', {'retval': {'already_cfretained': True}}), 'JSValueUnprotect': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectIsConstructor': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectMakeDate': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSPropertyNameArrayRelease': (b'v^{OpaqueJSPropertyNameArray=}',), 'JSClassRelease': (b'v^{OpaqueJSClass=}',), 'JSObjectCallAsFunction': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {4: {'c_array_length_in_arg': 3, 'type_modifier': 'n'}, 5: {'type_modifier': 'o'}}}), 'JSContextGroupRetain': (b'^{OpaqueJSContextGroup=}^{OpaqueJSContextGroup=}',), 'JSValueGetType': (b'I^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameArrayGetCount': (sel32or64(b'L^{OpaqueJSPropertyNameArray=}', b'Q^{OpaqueJSPropertyNameArray=}'),), 'JSValueToObject': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSStringGetLength': (sel32or64(b'L^{OpaqueJSString=}', b'Q^{OpaqueJSString=}'),), 'JSGarbageCollect': (b'v^{OpaqueJSContext=}',), 'JSStringRelease': (b'v^{OpaqueJSString=}',), 'JSGlobalContextRetain': (b'^{OpaqueJSContext=}^{OpaqueJSContext=}',)}
aliases = {'JSObjectRef': 'JSValueRef', 'JSGlobalContextRef': 'JSContextRef'}
misc.update({'JSValueRef': objc.createOpaquePointerType('JSValueRef', b'^{OpaqueJSValue=}'), 'JSStringRef': objc.createOpaquePointerType('JSStringRef', b'^{OpaqueJSString=}'), 'JSContextRef': objc.createOpaquePointerType('JSContextRef', b'^{OpaqueJSContext=}'), 'JSPropertyNameArrayRef': objc.createOpaquePointerType('JSPropertyNameArrayRef', b'^{OpaqueJSPropertyNameArray=}'), 'JSClassRef': objc.createOpaquePointerType('JSClassRef', b'^{OpaqueJSClass=}'), 'JSContextGroupRef': objc.createOpaquePointerType('JSContextGroupRef', b'^{OpaqueJSContextGroup=}'), 'JSPropertyNameAccumulatorRef': objc.createOpaquePointerType('JSPropertyNameAccumulatorRef', b'^{OpaqueJSPropertyNameAccumulator=}')})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'JSContext', b'exceptionHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'JSContext', b'setExceptionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'JSValue', b'deleteProperty:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'hasProperty:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isArray', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isBoolean', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isDate', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isEqualToObject:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isEqualWithTypeCoercionToObject:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isInstanceOf:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isNull', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isNumber', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isObject', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isString', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isUndefined', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'toBool', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'valueWithBool:inContext:', {'arguments': {2: {'type': 'Z'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE