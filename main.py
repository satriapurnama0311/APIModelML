import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask, jsonify

app = Flask(__name__)
    
@app.route('/') # Homepage
def home():
    return jsonify({'message': 'API ML for SmartHarvest Ready!'})

# Endpoint to return the predicted prices for items at a specific time
@app.route('/predicted-prices-jan', methods=['GET'])
def get_predicted_prices():
    # Replace this JSON structure with your actual data or load it from a file/database
    predicted_prices = {
        "2024-01-01": {
            "Beras Medium": 11457.058069821447,
            "Beras Premium": 12986.539254926145,
            "Gula Pasir": 14074.43890728429,
            "Minyak Goreng Curah": 13669.716233700514,
            "Minyak Goreng Kemasan Premium": 16558.252917051315,
            "Daging Sapi": 129165.65335541962,
            "Daging Ayam Ras": 35130.80072359741,
            "Telur Ayam Ras": 26758.227555394173,
            "Tepung Terigu Protein Sedang": 10149.267954550683,
            "Kedelai Impor": 12026.321229226887,
            "Cabai Merah Besar": 58302.07257771491,
            "Cabai Merah Keriting": 60038.29709124565,
            "Cabai Rawit Merah": 77710.6076657772,
            "Bawang Merah": 28016.77152490616,
            "Bawang Putih": 32484.209815382957
        },"2024-01-08": {
            "Beras Medium": 11581.788108810782,
            "Beras Premium": 12290.46509822458,
            "Gula Pasir": 13802.027360182256,
            "Minyak Goreng Curah": 13386.529093697667,
            "Minyak Goreng Kemasan Premium": 16153.895737290382,
            "Daging Sapi": 127484.09557837246,
            "Daging Ayam Ras": 34348.86501559615,
            "Telur Ayam Ras": 26143.23931670189,
            "Tepung Terigu Protein Sedang": 10513.660371512175,
            "Kedelai Impor": 11550.513001643121,
            "Cabai Merah Besar": 57506.04386508464,
            "Cabai Merah Keriting": 59383.51486849785,
            "Cabai Rawit Merah": 80004.08719778061,
            "Bawang Merah": 27047.035991102457,
            "Bawang Putih": 31738.867085933685
        },"2024-01-15": {
            "Beras Medium": 11051.753904309124,
            "Beras Premium": 12137.019623436034,
            "Gula Pasir": 13301.158589184284,
            "Minyak Goreng Curah": 12944.75765106827,
            "Minyak Goreng Kemasan Premium": 15809.325853586197,
            "Daging Sapi": 123454.44830161332,
            "Daging Ayam Ras": 33499.67050486803,
            "Telur Ayam Ras": 25136.88620853424,
            "Tepung Terigu Protein Sedang": 9932.279562041163,
            "Kedelai Impor": 11062.437078133225,
            "Cabai Merah Besar": 54499.40577328205,
            "Cabai Merah Keriting": 56624.005692601204,
            "Cabai Rawit Merah": 79703.89695167542,
            "Bawang Merah": 26526.184335649014,
            "Bawang Putih": 30584.220081806183
        },"2024-01-22": {
            "Beras Medium": 10818.886745393276,
            "Beras Premium": 12106.591838888824,
            "Gula Pasir": 13230.402265451849,
            "Minyak Goreng Curah": 12838.866625033319,
            "Minyak Goreng Kemasan Premium": 15696.246004343033,
            "Daging Sapi": 120459.50039470194,
            "Daging Ayam Ras": 32808.51092749834,
            "Telur Ayam Ras": 24576.785801142454,
            "Tepung Terigu Protein Sedang": 9784.664416195825,
            "Kedelai Impor": 11090.05299501121,
            "Cabai Merah Besar": 51716.74911868572,
            "Cabai Merah Keriting": 54259.679403722286,
            "Cabai Rawit Merah": 79640.56866168976,
            "Bawang Merah": 26339.98549759388,
            "Bawang Putih": 29759.2537689209
        },"2024-01-29": {
            "Beras Medium": 10671.92466076091,
            "Beras Premium": 12145.780704803765,
            "Gula Pasir": 13275.737709755078,
            "Minyak Goreng Curah": 12835.739328242838,
            "Minyak Goreng Kemasan Premium": 15638.182354688644,
            "Daging Sapi": 118021.6979075074,
            "Daging Ayam Ras": 32250.81699104607,
            "Telur Ayam Ras": 24159.341356247663,
            "Tepung Terigu Protein Sedang": 9747.388725303113,
            "Kedelai Impor": 11214.960971456021,
            "Cabai Merah Besar": 49077.86035215855,
            "Cabai Merah Keriting": 52001.358681082726,
            "Cabai Rawit Merah": 79630.12383580208,
            "Bawang Merah": 26379.023047089577,
            "Bawang Putih": 29131.068158626556
        }
        
    }

    # You can retrieve the predicted prices for a specific time or return all predictions
    return jsonify(predicted_prices)

@app.route('/predicted-prices-feb', methods=['GET'])
def get_predicted_prices_feb():
  predicted_prices_feb = {
    "2024-02-05": {
        "Beras Medium": 10586.678457960486,
        "Beras Premium": 12217.107929468155,
        "Gula Pasir": 13343.952180683613,
        "Minyak Goreng Curah": 12877.432269878685,
        "Minyak Goreng Kemasan Premium": 15589.067887961864,
        "Daging Sapi": 116058.04131370781,
        "Daging Ayam Ras": 31801.458240911365,
        "Telur Ayam Ras": 23813.36145505309,
        "Tepung Terigu Protein Sedang": 9778.709505306557,
        "Kedelai Impor": 11353.476235195994,
        "Cabai Merah Besar": 46568.029089689255,
        "Cabai Merah Keriting": 49828.3849927783,
        "Cabai Rawit Merah": 79587.09822893143,
        "Bawang Merah": 26517.418008744717,
        "Bawang Putih": 28661.964399576187
    },"2024-02-12": {
        "Beras Medium": 10550.3388620466,
        "Beras Premium": 12312.225431933999,
        "Gula Pasir": 13423.70000676997,
        "Minyak Goreng Curah": 12954.972791425884,
        "Minyak Goreng Kemasan Premium": 15545.972675442696,
        "Daging Sapi": 114505.16847413777,
        "Daging Ayam Ras": 31429.706329643726,
        "Telur Ayam Ras": 23516.723836570978,
        "Tepung Terigu Protein Sedang": 9864.830161849037,
        "Kedelai Impor": 11499.384669810534,
        "Cabai Merah Besar": 44206.486718058586,
        "Cabai Merah Keriting": 47753.460696041584,
        "Cabai Rawit Merah": 79479.8598587513,
        "Bawang Merah": 26670.095919430256,
        "Bawang Putih": 28357.89041030407
    },"2024-02-19": {
        "Beras Medium": 10568.052684597671,
        "Beras Premium": 12427.698382623494,
        "Gula Pasir": 13511.52314808406,
        "Minyak Goreng Curah": 13054.460491366684,
        "Minyak Goreng Kemasan Premium": 15513.707325085998,
        "Daging Sapi": 113338.42230361699,
        "Daging Ayam Ras": 31124.900892317295,
        "Telur Ayam Ras": 23281.13605543971,
        "Tepung Terigu Protein Sedang": 9991.776723083109,
        "Kedelai Impor": 11651.277563869953,
        "Cabai Merah Besar": 41991.60293626785,
        "Cabai Merah Keriting": 45778.335419118404,
        "Cabai Rawit Merah": 79299.65243935585,
        "Bawang Merah": 26788.985803723335,
        "Bawang Putih": 28186.712965607643
    },"2024-02-26": {
        "Beras Medium": 10604.728421773762,
        "Beras Premium": 12556.019237674773,
        "Gula Pasir": 13611.610071856529,
        "Minyak Goreng Curah": 13180.661116033792,
        "Minyak Goreng Kemasan Premium": 15493.254558488727,
        "Daging Sapi": 112470.30197197197,
        "Daging Ayam Ras": 30882.549199476838,
        "Telur Ayam Ras": 23089.849304884672,
        "Tepung Terigu Protein Sedang": 10135.400098398328,
        "Kedelai Impor": 11800.232632383704,
        "Cabai Merah Besar": 39940.800729990005,
        "Cabai Merah Keriting": 43908.87027621269,
        "Cabai Rawit Merah": 79050.58475136757,
        "Bawang Merah": 26872.152905881405,
        "Bawang Putih": 28124.399306058884
    }
  }
  
  return jsonify(predicted_prices_feb)

@app.route('/predicted-prices-mar', methods=['GET'])
def get_predicted_prices_mar():
  predicted_prices_mar = {
    "2024-03-04": {
        "Beras Medium": 10638.870337363333,
        "Beras Premium": 12676.682055957615,
        "Gula Pasir": 13693.269364411011,
        "Minyak Goreng Curah": 13313.806287884712,
        "Minyak Goreng Kemasan Premium": 15488.983603149652,
        "Daging Sapi": 111801.25013506411,
        "Daging Ayam Ras": 30675.205788105726,
        "Telur Ayam Ras": 22897.937534958124,
        "Tepung Terigu Protein Sedang": 10230.229345917702,
        "Kedelai Impor": 11955.689445957541,
        "Cabai Merah Besar": 38083.829667449,
        "Cabai Merah Keriting": 42085.389744699,
        "Cabai Rawit Merah": 78743.90568733215,
        "Bawang Merah": 26910.265881836414,
        "Bawang Putih": 28104.368562459946
    },"2024-03-11": {
        "Beras Medium": 10634.455076459795,
        "Beras Premium": 12766.217212170362,
        "Gula Pasir": 13712.221355643123,
        "Minyak Goreng Curah": 13416.493476420641,
        "Minyak Goreng Kemasan Premium": 15493.039440393448,
        "Daging Sapi": 111145.34292662142,
        "Daging Ayam Ras": 30466.57359147072,
        "Telur Ayam Ras": 22648.605320990086,
        "Tepung Terigu Protein Sedang": 10226.165425594896,
        "Kedelai Impor": 12097.471635919064,
        "Cabai Merah Besar": 36422.234424591064,
        "Cabai Merah Keriting": 40248.788405537605,
        "Cabai Rawit Merah": 78386.42569184303,
        "Bawang Merah": 26908.122240960598,
        "Bawang Putih": 28026.346474170685
    },"2024-03-18": {
        "Beras Medium": 10611.899002753198,
        "Beras Premium": 12836.326812408864,
        "Gula Pasir": 13693.800137307495,
        "Minyak Goreng Curah": 13484.519031137228,
        "Minyak Goreng Kemasan Premium": 15486.61696639657,
        "Daging Sapi": 110475.68030846117,
        "Daging Ayam Ras": 30269.676033496857,
        "Telur Ayam Ras": 22391.03655037284,
        "Tepung Terigu Protein Sedang": 10201.6744559668,
        "Kedelai Impor": 12202.553303353488,
        "Cabai Merah Besar": 34869.790573596954,
        "Cabai Merah Keriting": 38488.22989785671,
        "Cabai Rawit Merah": 77907.71656632423,
        "Bawang Merah": 26894.64743769169,
        "Bawang Putih": 27892.50969696045
    },"2024-03-25": {
        "Beras Medium": 10576.956750825047,
        "Beras Premium": 12894.431396823376,
        "Gula Pasir": 13644.528465813026,
        "Minyak Goreng Curah": 13522.7919947505,
        "Minyak Goreng Kemasan Premium": 15473.132067397237,
        "Daging Sapi": 109791.08177900313,
        "Daging Ayam Ras": 30082.772996664047,
        "Telur Ayam Ras": 22131.942903727293,
        "Tepung Terigu Protein Sedang": 10163.583361417055,
        "Kedelai Impor": 12278.15192040056,
        "Cabai Merah Besar": 33409.8252042532,
        "Cabai Merah Keriting": 36799.19271045923,
        "Cabai Rawit Merah": 77280.76167106628,
        "Bawang Merah": 26851.873926222324,
        "Bawang Putih": 27709.63617157936
    }
  }
  
  return jsonify(predicted_prices_mar)

if __name__ == '__main__':
    app.run(debug=True)