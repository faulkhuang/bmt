import unittest

import testmodule
from common import gobject, testhelper
from gobject import GObject, GInterface

class TestSubType(unittest.TestCase):
    def testSubType(self):
        t = type('testtype', (GObject, GInterface), {})
        self.failUnless(issubclass(t, GObject))
        self.failUnless(issubclass(t, GInterface))
        
    def testGObject(self):
        label = gobject.GObject()
        self.assertEqual(label.__grefcount__, 1)
        label = gobject.new(gobject.GObject)
        self.assertEqual(label.__grefcount__, 1)

    def testPythonSubclass(self):
        label = testmodule.PyGObject()
        self.assertEqual(label.__grefcount__, 1)
        self.assertEqual(label.props.label, "hello")
        label = gobject.new(testmodule.PyGObject)
        self.assertEqual(label.__grefcount__, 1)
        self.assertEqual(label.props.label, "hello")

    def testCPyCSubclassing(self):
        obj = testhelper.create_test_type()
        self.assertEqual(obj.__grefcount__, 1)
        refcount = testhelper.test_g_object_new()
        self.assertEqual(refcount, 2)
        
    def testRegisterArgNotType(self):
        self.assertRaises(TypeError, gobject.type_register, 1)

    def testGObjectNewError(self):
        self.assertRaises(TypeError, gobject.new, gobject.GObject, text='foo')
