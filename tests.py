# -*- coding: utf-8 -*-
# Author: ZhangTianJie

import unittest

from registry import Registry


class TestRegistry(unittest.TestCase):

    def test_set(self):
        registry = Registry()
        registry.set('a', 'a')
        registry.set('b', [1, 2])
        registry.set('c.h', 'h')
        self.assertEqual(registry.get(), {
            'a': 'a',
            'b': [1, 2],
            'c': {
                'h': 'h'
            }
        })

    def test_merge(self):
        registry = Registry()
        registry.load({
            'a': {
                'h': 'h',
                'i': 'i',
            }
        })
        registry.merge('a', {
            'g': 'g',
        })
        self.assertEqual(registry.get(), {
            'a': {
                'h': 'h',
                'i': 'i',
                'g': 'g',
            }
        })

    def test_get(self):
        registry = Registry()
        registry.load({'a': {'aa': 'aaa'}})
        self.assertEqual(registry.get(), {'a': {'aa': 'aaa'}})
        self.assertEqual(registry.get('a'), {'aa': 'aaa'})
        self.assertEqual(registry.get('a.aa'), 'aaa')
        self.assertEqual(registry.get('b', ['b']), ['b'])

    def test_load(self):
        d = {
            'a': 'a',
            'b': 1,
            'c': {
                'h': 'h',
                'i': 'i',
                'g': 'g',
            },
            'd': [1, 2],
            'e': True,
            'f': 1.1,
        }
        registry = Registry()
        registry.load(d)
        self.assertEqual(registry.get(), d)

    def test_default(self):
        registry = Registry()
        registry.set('a', 'aaa')
        self.assertEqual(registry.default('a', 'bbb'), 'aaa')
        self.assertEqual(registry.get('a'), 'aaa')
        self.assertEqual(registry.default('c', 'ccc'), 'ccc')
        self.assertEqual(registry.get('c', 'ccc'), 'ccc')


if __name__ == '__main__':
    unittest.main()
