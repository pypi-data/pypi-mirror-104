import json
import logging
import os
import sqlite3
from sqlite3 import Connection, DatabaseError
from typing import Optional, List

import pandas as pd
from pandas.io.sql import DatabaseError as PandasDatabaseError

from pyridy.utils import Sensor, AccelerationSeries, LinearAccelerationSeries, MagnetometerSeries, OrientationSeries, \
    GyroSeries, RotationSeries, GPSSeries, PressureSeries, HumiditySeries, TemperatureSeries, WzSeries, LightSeries, \
    SubjectiveComfortSeries
from pyridy.utils.device import Device

logger = logging.getLogger(__name__)


class RDYFile:
    def __init__(self, path: str = ""):
        self.path = path
        self.filename: Optional[str] = ""
        self.extension: Optional[str] = ""

        self.db_con: Optional[Connection] = None

        # RDY File Infos
        self.rdy_format_version: Optional[float] = None
        self.rdy_info_name: Optional[str] = None
        self.rdy_info_sex: Optional[str] = None
        self.rdy_info_age: Optional[int] = None
        self.rdy_info_height: Optional[float] = None
        self.rdy_info_weight: Optional[float] = None

        self.t0: Optional[str] = None
        self.timestamp_when_started: Optional[int] = None
        self.timestamp_when_stopped: Optional[int] = None
        self.device: Optional[Device] = None

        # Sensors
        self.sensors: Optional[List[Sensor]] = []

        # Measurement Series
        self.acc_series: Optional[AccelerationSeries] = None
        self.lin_acc_series: Optional[LinearAccelerationSeries] = None
        self.mag_series: Optional[MagnetometerSeries] = None
        self.orient_series: Optional[OrientationSeries] = None
        self.gyro_series: Optional[GyroSeries] = None
        self.rot_series: Optional[RotationSeries] = None
        self.gps_series: Optional[GPSSeries] = None
        self.pressure_series: Optional[PressureSeries] = None
        self.temperature_series: Optional[TemperatureSeries] = None
        self.humidity_series: Optional[HumiditySeries] = None
        self.light_series: Optional[LightSeries] = None
        self.wz_series: Optional[WzSeries] = None
        self.subjective_comfort_series: Optional[SubjectiveComfortSeries] = None

        if self.path:
            self.load_file(self.path)
        pass

    def __repr__(self):
        return "%s" % self.filename

    def load_file(self, path: str):
        logger.info("Loading file: %s" % path)

        _, self.extension = os.path.splitext(path)
        _, self.filename = os.path.split(path)

        if self.extension == ".rdy":
            with open(path, 'r') as file:
                rdy = json.load(file)

            if 'RDY_Format_Version' in rdy:
                self.rdy_format_version = rdy['RDY_Format_Version']
            else:
                logger.info("No RDY_Format_Version in file: %s" % self.filename)
                self.rdy_format_version = None

            if 'RDY_Info_Name' in rdy:
                self.rdy_info_name = rdy['RDY_Info_Name']
            else:
                logger.info("No RDY_Info_Name in file: %s" % self.filename)
                self.rdy_info_name = None

            if 'RDY_Info_Sex' in rdy:
                self.rdy_info_sex = rdy['RDY_Info_Sex']
            else:
                logger.info("No RDY_Info_Sex in file: %s" % self.filename)
                self.rdy_info_sex = None

            if 'RDY_Info_Age' in rdy:
                self.rdy_info_age = rdy['RDY_Info_Age']
            else:
                logger.info("No RDY_Info_Age in file: %s" % self.filename)
                self.rdy_info_age = None

            if 'RDY_Info_Height' in rdy:
                self.rdy_info_height = rdy['RDY_Info_Height']
            else:
                logger.info("No RDY_Info_Height in file: %s" % self.filename)
                self.rdy_info_height = None

            if 'RDY_Info_Weight' in rdy:
                self.rdy_info_weight = rdy['RDY_Info_Weight']
            else:
                logger.info("No RDY_Info_Weight in file: %s" % self.filename)
                self.rdy_info_weight = None

            if 't0' in rdy:
                self.t0 = rdy['t0']
            else:
                self.t0 = None
                logger.info("No t0 in file: %s" % self.filename)

            if 'timestamp_when_started' in rdy:
                self.timestamp_when_started = rdy['timestamp_when_started']
            else:
                self.timestamp_when_started = None
                logger.info("No timestamp_when_started in file: %s" % self.filename)

            if 'timestamp_when_stopped' in rdy:
                self.timestamp_when_stopped = rdy['timestamp_when_stopped']
            else:
                self.timestamp_when_stopped = None
                logger.info("No timestamp_when_stopped in file: %s" % self.filename)

            if "device" in rdy:
                self.device = Device(**rdy['device_info'])
            else:
                logger.info("No device information in file: %s" % self.filename)

            if "sensors" in rdy:
                for sensor in rdy['sensors']:
                    self.sensors.append(Sensor(**sensor))
            else:
                logger.info("No sensor descriptions in file: %s" % self.filename)

            if "acc_series" in rdy:
                self.acc_series = AccelerationSeries(**rdy['acc_series'])
            else:
                logger.info("No Acceleration Series in file: %s" % self.filename)
                self.acc_series = AccelerationSeries()

            if "lin_acc_series" in rdy:
                self.lin_acc_series = LinearAccelerationSeries(**rdy['lin_acc_series'])
            else:
                logger.info("No Linear Acceleration Series in file: %s" % self.filename)
                self.lin_acc_series = LinearAccelerationSeries()

            if "mag_series" in rdy:
                self.mag_series = MagnetometerSeries(**rdy['mag_series'])
            else:
                logger.info("No Magnetometer Series in file: %s" % self.filename)
                self.mag_series = MagnetometerSeries()

            if "orient_series" in rdy:
                self.orient_series = OrientationSeries(**rdy['orient_series'])
            else:
                logger.info("No Orientation Series in file: %s" % self.filename)
                self.orient_series = OrientationSeries()

            if "gyro_series" in rdy:
                self.gyro_series = GyroSeries(**rdy['gyro_series'])
            else:
                logger.info("No Gyro Series in file: %s" % self.filename)
                self.gyro_series = GyroSeries()

            if "rot_series" in rdy:
                self.rot_series = RotationSeries(**rdy['rot_series'])
            else:
                logger.info("No Rotation Series in file: %s" % self.filename)
                self.rot_series = RotationSeries()

            if "gps_series" in rdy:
                self.gps_series = GPSSeries(**rdy['gps_series'])
            else:
                logger.info("No GPS Series in file: %s" % self.filename)
                self.gps_series = GPSSeries()

            if "pressure_series" in rdy:
                self.pressure_series = PressureSeries(**rdy['pressure_series'])
            else:
                logger.info("No Pressure Series in file: %s" % self.filename)
                self.pressure_series = PressureSeries()

            if "temperature_series" in rdy:
                self.temperature_series = TemperatureSeries(**rdy['temperature_series'])
            else:
                logger.info("No Temperature Series in file: %s" % self.filename)
                self.temperature_series = TemperatureSeries()

            if "humidity_series" in rdy:
                self.humidity_series = HumiditySeries(**rdy['humidity_series'])
            else:
                logger.info("No Humidity Series in file: %s" % self.filename)
                self.humidity_series = HumiditySeries()

            if "light_series" in rdy:
                self.light_series = LightSeries(**rdy['light_series'])
            else:
                logger.info("No Light Series in file: %s" % self.filename)
                self.light_series = LightSeries()

            if "wz_series" in rdy:
                self.wz_series = WzSeries(**rdy['wz_series'])
            else:
                logger.info("No Wz Series in file: %s" % self.filename)
                self.wz_series = WzSeries()

            if "subjective_comfort_series" in rdy:
                self.subjective_comfort_series = SubjectiveComfortSeries(**rdy['subjective_comfort_series'])
            else:
                logger.info("No Subjective Comfort Series in file: %s" % self.filename)
                self.subjective_comfort_series = SubjectiveComfortSeries()
            pass

        elif self.extension == ".sqlite":
            self.db_con = sqlite3.connect(path)

            try:
                info = dict(pd.read_sql_query("SELECT * from measurement_information_table", self.db_con))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing measurement_information_table, file: %s" % self.filename)
                try:
                    info = dict(pd.read_sql_query("SELECT * from measurment_information_table", self.db_con))  # Older files can contain wrong table name
                except (DatabaseError, PandasDatabaseError) as e:
                    info = None

            try:
                sensor_df = pd.read_sql_query("SELECT * from sensor_descriptions_table", self.db_con)
                for _, row in sensor_df.iterrows():
                    self.sensors.append(Sensor(**dict(row)))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing sensor_descriptions_table, file: %s" % self.filename)

            try:
                device_df = pd.read_sql_query("SELECT * from device_information_table", self.db_con)
                self.device = Device(**dict(device_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing device_information_table, file: %s" % self.filename)
                self.device = Device()

            # Info
            if info is not None:
                self.rdy_format_version = info['rdy_format_version'][0] if len(info['rdy_format_version']) > 0 else None
                self.rdy_info_name = info['rdy_info_name'][0] if len(info['rdy_info_name']) > 0 else None
                self.rdy_info_sex = info['rdy_info_sex'][0] if len(info['rdy_info_sex']) > 0 else None
                self.rdy_info_age = info['rdy_info_age'][0] if len(info['rdy_info_age']) > 0 else None
                self.rdy_info_height = info['rdy_info_height'][0] if len(info['rdy_info_height']) > 0 else None
                self.rdy_info_weight = info['rdy_info_weight'][0] if len(info['rdy_info_weight']) > 0 else None

                self.t0 = info['t0'][0] if len(info['t0']) > 0 else None
                self.timestamp_when_started = info['timestamp_when_started'][0] if len(info['timestamp_when_started']) > 0 else None
                self.timestamp_when_stopped = info['timestamp_when_stopped'][0] if len(info['timestamp_when_stopped']) > 0 else None

            # Measurements
            try:
                acc_df = pd.read_sql_query("SELECT * from acc_measurements_table", self.db_con)
                self.acc_series = AccelerationSeries(**dict(acc_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing acc_measurements_table, file: %s" % self.filename)
                self.acc_series = AccelerationSeries()

            try:
                lin_acc_df = pd.read_sql_query("SELECT * from lin_acc_measurements_table", self.db_con)
                self.lin_acc_series = LinearAccelerationSeries(**dict(lin_acc_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing lin_acc_measurements_table, file: %s" % self.filename)
                self.lin_acc_series = LinearAccelerationSeries()

            try:
                mag_df = pd.read_sql_query("SELECT * from mag_measurements_table", self.db_con)
                self.mag_series = MagnetometerSeries(**dict(mag_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing mag_measurements_table, file: %s" % self.filename)
                self.mag_series = MagnetometerSeries()

            try:
                orient_df = pd.read_sql_query("SELECT * from orient_measurements_table", self.db_con)
                self.orient_series = OrientationSeries(**dict(orient_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing orient_measurements_table, file: %s" % self.filename)
                self.orient_series = OrientationSeries()

            try:
                gyro_df = pd.read_sql_query("SELECT * from gyro_measurements_table", self.db_con)
                self.gyro_series = GyroSeries(**dict(gyro_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing gyro_measurements_table, file: %s" % self.filename)
                self.gyro_series = GyroSeries()

            try:
                rot_df = pd.read_sql_query("SELECT * from rot_measurements_table", self.db_con)
                self.rot_series = RotationSeries(**dict(rot_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing rot_measurements_table, file: %s" % self.filename)
                self.rot_series = RotationSeries()

            try:
                gps_df = pd.read_sql_query("SELECT * from gps_measurements_table", self.db_con)
                self.gps_series = GPSSeries(**dict(gps_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing gps_measurements_table, file: %s" % self.filename)
                self.gps_series = GPSSeries()

            try:
                pressure_df = pd.read_sql_query("SELECT * from pressure_measurements_table", self.db_con)
                self.pressure_series = PressureSeries(**dict(pressure_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing pressure_measurements_table, file: %s" % self.filename)
                self.pressure_series = PressureSeries()

            try:
                temperature_df = pd.read_sql_query("SELECT * from temperature_measurements_table", self.db_con)
                self.temperature_series = TemperatureSeries(**dict(temperature_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing temperature_measurements_table, file: %s" % self.filename)
                self.temperature_series = TemperatureSeries()

            try:
                humidity_df = pd.read_sql_query("SELECT * from humidity_measurements_table", self.db_con)
                self.humidity_series = HumiditySeries(**dict(humidity_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing humidity_measurements_table, file: %s" % self.filename)
                self.humidity_series = HumiditySeries()

            try:
                light_df = pd.read_sql_query("SELECT * from light_measurements_table", self.db_con)
                self.light_series = LightSeries(**dict(light_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing light_measurements_table, file: %s" % self.filename)
                self.light_series = LightSeries()

            try:
                wz_df = pd.read_sql_query("SELECT * from wz_measurements_table", self.db_con)
                self.wz_series = WzSeries(**dict(wz_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing wz_measurements_table, file: %s" % self.filename)
                self.wz_series = WzSeries()

            try:
                subjective_comfort_df = pd.read_sql_query("SELECT * from subjective_comfort_measurements_table",
                                                          self.db_con)
                self.subjective_comfort_series = SubjectiveComfortSeries(**dict(subjective_comfort_df))
            except (DatabaseError, PandasDatabaseError) as e:
                logger.error("DatabaseError occurred when accessing subjective_comfort_measurements_table, file: %s" % self.filename)
                self.subjective_comfort_series = SubjectiveComfortSeries()

        else:
            raise ValueError("File extension %s is not supported" % self.extension)
