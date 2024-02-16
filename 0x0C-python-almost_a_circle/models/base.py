#!/usr/bin/python3
"""
base module

This module defines the Base class,
which serves as the base class for other classes.
It provides common functionality such as JSON serialization
and deserialization.

Attributes:
    id (int): The identifier of the instance.
    __nb_objects (int): A class variable to keep track of the number
    of instances created.

Methods:
    __init__: Initializes a new instance of the Base class.
    to_json_string: Converts a list of dictionaries to a JSON-formatted string.
    save_to_file: Saves a list of instances to a file in JSON format.
    from_json_string: Converts a JSON-formatted string to
    a list of dictionaries.
    create: Creates a new instance from a dictionary.
    update: Updates the attributes of an instance.
    load_from_file: Loads instances from a file and
    returns a list of instances.
"""
import json


class Base:
    """
    Base class for other classes.

    Attributes:
        id (int): The identifier of the instance.
        __nb_objects (int): A class variable to keep track of
                            the number of instances created.

    Methods:
        __init__: Initializes a new instance of the Base class.
        to_json_string: Converts a list of dictionaries to
                        a JSON-formatted string.
        save_to_file: Saves a list of instances to a file in JSON format.
        from_json_string: Converts a JSON-formatted string to
                          a list of dictionaries.
        create: Creates a new instance from a dictionary.
        update: Updates the attributes of an instance.
        load_from_file: Loads instances from a file and
                        returns a list of instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The identifier of the instance.
                      If not provided, a unique identifier is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries representing
                                      instances.

        Returns:
            str: A JSON-formatted string.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a file in JSON format.

        Args:
            list_objs (list): A list of instances.

        Note:
            The file name "Rectangle.json" is hardcoded.

        Example:
            save_to_file([instance1, instance2])
        """
        if list_objs:
            listObjs = [i.to_dictionary() for i in list_objs]
            with open("Rectangle.json", "w") as file:
                file.write(cls.to_json_string(listObjs))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: A list of dictionaries representing instances.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class using a dictionary of attributes.

        Args:
            dictionary (dict): A dictionary containing attributes
                               for the instance.

        Returns:
            cls: A new instance of the class with attributes set
                 from the dictionary.
        """
        """args_tuple = ()
        for k, v in dictionary.items():
            args_tuple += (v,)
        print(args_tuple)
        # return cls.update(args_tuple)
        return cls(*args_tuple)"""
        return cls(**dictionary)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of an instance using
        arguments or keyword arguments.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.

        Note:
            If both args and kwargs are provided, args take precedence.

        Example:
            obj.update(id=10, width=5, height=10) will update id to 10,
            width to 5, and height to 10.
        """
        pass
        """if args:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.__width = args[1]
            except IndexError:
                pass
            try:
                self.__height = args[2]
            except IndexError:
                pass
            try:
                self.__x = args[3]
            except IndexError:
                pass
            try:
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = vi
        return self.id, self.__width, self.__height, self.__x, self.__y"""

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of objects from a file in JSON format.

        Returns:
            list: A list of instances loaded from the file.
        """
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                return [cls.create(**obj) for obj in data]
        except FileNotFoundError:
            return []
